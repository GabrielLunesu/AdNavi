"""Meta Ads API Client Service.

WHAT:
    Wrapper for Facebook Business SDK providing rate-limited access to Meta Marketing API.
    Handles campaigns, adsets, ads, and insights fetching with automatic pagination.

WHY:
    - Centralized Meta API interaction (single source of truth)
    - Rate limiting enforcement (200 calls/hour per account)
    - Pagination handling (Meta returns max 100 records per call)
    - Graceful error handling (400/401/403 responses)

WHERE USED:
    - app/routers/meta_sync.py (sync endpoints call this service)
    - app/services/meta_metrics_fetcher.py (Phase 3, automated sync)

DEPENDENCIES:
    - facebook_business SDK
    - app/deps.py (META_ACCESS_TOKEN from .env)
    
RATE LIMITS:
    - 200 API calls per hour per ad account
    - Implements decorator: @rate_limit(calls_per_hour=200)

REFERENCES:
    - backend/test_meta_api.py (test patterns)
    - backend/app/models.py (Connection, Entity)
    - https://developers.facebook.com/docs/marketing-api
"""

import logging
from functools import wraps
from time import time, sleep
from collections import deque
from typing import List, Dict, Any, Optional
from datetime import datetime

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.exceptions import FacebookRequestError

logger = logging.getLogger(__name__)


def rate_limit(calls_per_hour: int):
    """Decorator to enforce rate limiting using sliding window algorithm.
    
    WHAT:
        Tracks API call timestamps in a deque and enforces maximum calls per hour.
        Sleeps if rate limit would be exceeded.
    
    WHY:
        Meta enforces 200 calls/hour per ad account. Exceeding this causes 429 errors.
        Proactive rate limiting prevents API throttling and ensures reliable syncs.
    
    Args:
        calls_per_hour: Maximum number of calls allowed per hour
        
    Returns:
        Decorated function that enforces rate limiting
    """
    call_times = deque(maxlen=calls_per_hour)
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time()
            
            # Remove calls older than 1 hour (3600 seconds)
            while call_times and call_times[0] < now - 3600:
                call_times.popleft()
            
            # If at limit, sleep until oldest call expires
            if len(call_times) >= calls_per_hour:
                sleep_time = 3600 - (now - call_times[0]) + 1
                logger.warning(
                    f"[META_CLIENT] Rate limit reached ({calls_per_hour} calls/hour). "
                    f"Sleeping for {sleep_time:.1f}s"
                )
                sleep(sleep_time)
            
            call_times.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator


class MetaAdsClientError(Exception):
    """Base exception for Meta Ads Client errors."""
    pass


class MetaAdsAuthenticationError(MetaAdsClientError):
    """Raised when authentication fails (401)."""
    pass


class MetaAdsPermissionError(MetaAdsClientError):
    """Raised when permissions are insufficient (403)."""
    pass


class MetaAdsValidationError(MetaAdsClientError):
    """Raised when request is malformed (400)."""
    pass


class MetaAdsClient:
    """Client for interacting with Meta Marketing API.
    
    WHAT:
        Provides methods to fetch campaigns, adsets, ads, and insights from Meta.
        Handles rate limiting, pagination, and error responses automatically.
    
    WHY:
        Centralizes all Meta API interactions in one place.
        Ensures consistent error handling and rate limiting across all sync operations.
    
    Usage:
        ```python
        client = MetaAdsClient(access_token="YOUR_TOKEN")
        campaigns = client.get_campaigns("act_123456789")
        insights = client.get_insights("123456", "2024-01-01", "2024-01-07", level="ad")
        ```
    """
    
    def __init__(self, access_token: str, app_id: Optional[str] = None, app_secret: Optional[str] = None):
        """Initialize Meta Ads client with access token.
        
        WHAT:
            Initializes FacebookAdsApi with provided credentials.
            For system user tokens, app_id and app_secret are optional.
        
        WHY:
            System user tokens (used in Phase 2) don't require app credentials.
            OAuth tokens (Phase 7) will need app_id and app_secret.
        
        Args:
            access_token: Meta access token (system user or OAuth)
            app_id: Optional Meta app ID
            app_secret: Optional Meta app secret
        """
        self.access_token = access_token
        
        # Initialize Facebook Ads API
        FacebookAdsApi.init(
            app_id=app_id,
            app_secret=app_secret,
            access_token=access_token
        )
        
        logger.info("[META_CLIENT] Initialized with access token")
    
    @rate_limit(calls_per_hour=200)
    def get_campaigns(self, account_id: str) -> List[Dict[str, Any]]:
        """Fetch all campaigns for an ad account.
        
        WHAT:
            Retrieves all campaigns from Meta, handles pagination automatically.
            Returns campaign metadata (id, name, status, objective, etc.)
        
        WHY:
            First step in entity sync - campaigns are the top level of hierarchy.
        
        Args:
            account_id: Meta ad account ID (format: "act_123456789")
            
        Returns:
            List of campaign dictionaries with fields:
                - id: Campaign ID
                - name: Campaign name
                - status: ACTIVE, PAUSED, DELETED, ARCHIVED
                - objective: Campaign objective (e.g., OUTCOME_SALES)
                - daily_budget: Daily budget in cents (optional)
                - lifetime_budget: Lifetime budget in cents (optional)
                - created_time: Creation timestamp
                
        Raises:
            MetaAdsAuthenticationError: Invalid or expired token
            MetaAdsPermissionError: Insufficient permissions for account
            MetaAdsValidationError: Invalid account ID format
            MetaAdsClientError: Other API errors
        """
        try:
            logger.info(f"[META_CLIENT] Fetching campaigns for account: {account_id}")
            
            account = AdAccount(account_id)
            campaigns = account.get_campaigns(fields=[
                Campaign.Field.id,
                Campaign.Field.name,
                Campaign.Field.status,
                Campaign.Field.objective,
                Campaign.Field.daily_budget,
                Campaign.Field.lifetime_budget,
                Campaign.Field.created_time,
            ])
            
            # SDK iterator handles pagination automatically
            result = []
            for campaign in campaigns:
                result.append(dict(campaign))
            
            logger.info(f"[META_CLIENT] Fetched {len(result)} campaigns")
            return result
            
        except FacebookRequestError as e:
            return self._handle_api_error(e, f"fetching campaigns for {account_id}")
    
    @rate_limit(calls_per_hour=200)
    def get_adsets(self, campaign_id: str) -> List[Dict[str, Any]]:
        """Fetch all adsets for a campaign.
        
        WHAT:
            Retrieves all adsets belonging to a campaign.
            Returns adset metadata (id, name, status, targeting, etc.)
        
        WHY:
            Second level of entity hierarchy - adsets belong to campaigns.
        
        Args:
            campaign_id: Meta campaign ID
            
        Returns:
            List of adset dictionaries with fields:
                - id: AdSet ID
                - name: AdSet name
                - status: ACTIVE, PAUSED, DELETED, ARCHIVED
                - campaign_id: Parent campaign ID
                - daily_budget: Daily budget in cents (optional)
                - lifetime_budget: Lifetime budget in cents (optional)
                - targeting: Targeting configuration
                
        Raises:
            MetaAdsAuthenticationError: Invalid or expired token
            MetaAdsPermissionError: Insufficient permissions
            MetaAdsValidationError: Invalid campaign ID
            MetaAdsClientError: Other API errors
        """
        try:
            logger.info(f"[META_CLIENT] Fetching adsets for campaign: {campaign_id}")
            
            campaign = Campaign(campaign_id)
            adsets = campaign.get_ad_sets(fields=[
                AdSet.Field.id,
                AdSet.Field.name,
                AdSet.Field.status,
                AdSet.Field.campaign_id,
                AdSet.Field.daily_budget,
                AdSet.Field.lifetime_budget,
                AdSet.Field.targeting,
            ])
            
            result = []
            for adset in adsets:
                result.append(dict(adset))
            
            logger.info(f"[META_CLIENT] Fetched {len(result)} adsets")
            return result
            
        except FacebookRequestError as e:
            return self._handle_api_error(e, f"fetching adsets for campaign {campaign_id}")
    
    @rate_limit(calls_per_hour=200)
    def get_ads(self, adset_id: str) -> List[Dict[str, Any]]:
        """Fetch all ads for an adset.
        
        WHAT:
            Retrieves all ads belonging to an adset.
            Returns ad metadata (id, name, status, creative, etc.)
        
        WHY:
            Third level of entity hierarchy - ads belong to adsets.
            Ad-level metrics are most granular and avoid double-counting.
        
        Args:
            adset_id: Meta adset ID
            
        Returns:
            List of ad dictionaries with fields:
                - id: Ad ID
                - name: Ad name
                - status: ACTIVE, PAUSED, DELETED, ARCHIVED
                - adset_id: Parent adset ID
                - creative: Creative configuration
                
        Raises:
            MetaAdsAuthenticationError: Invalid or expired token
            MetaAdsPermissionError: Insufficient permissions
            MetaAdsValidationError: Invalid adset ID
            MetaAdsClientError: Other API errors
        """
        try:
            logger.info(f"[META_CLIENT] Fetching ads for adset: {adset_id}")
            
            adset = AdSet(adset_id)
            ads = adset.get_ads(fields=[
                Ad.Field.id,
                Ad.Field.name,
                Ad.Field.status,
                Ad.Field.adset_id,
                Ad.Field.creative,
            ])
            
            result = []
            for ad in ads:
                result.append(dict(ad))
            
            logger.info(f"[META_CLIENT] Fetched {len(result)} ads")
            return result
            
        except FacebookRequestError as e:
            return self._handle_api_error(e, f"fetching ads for adset {adset_id}")
    
    @rate_limit(calls_per_hour=200)
    def get_insights(
        self,
        entity_id: str,
        start_date: str,  # YYYY-MM-DD
        end_date: str,    # YYYY-MM-DD
        level: str = "ad",  # account/campaign/adset/ad
        time_increment: int = 1  # 1=daily
    ) -> List[Dict[str, Any]]:
        """Fetch insights (metrics) for entity and date range.
        
        WHAT:
            Retrieves performance metrics for a specific entity over a date range.
            Returns daily breakdown with spend, impressions, clicks, conversions, etc.
        
        WHY:
            This is where we get the actual metrics data for ingestion.
            Meta's Insights API provides aggregated performance data.
        
        CRITICAL NOTES:
            - Maximum 93 days per request (Meta API limit)
            - Hourly breakdowns ONLY available for last 3 days
            - For AdNavi Phase 2: Use daily breakdowns, chunk in 7-day windows
            - Actions array contains conversions/leads/purchases (complex parsing needed)
        
        Args:
            entity_id: Meta entity ID (account/campaign/adset/ad ID)
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            level: Aggregation level (account/campaign/adset/ad)
            time_increment: 1=daily, hourly=not used in Phase 2
            
        Returns:
            List of insight dictionaries with fields:
                - date_start: Period start date
                - date_stop: Period end date
                - spend: Ad spend (string, needs conversion)
                - impressions: Number of impressions (string)
                - clicks: Number of clicks (string)
                - actions: Array of conversion actions (complex structure)
                - action_values: Array of conversion values (revenue)
                
        Raises:
            MetaAdsAuthenticationError: Invalid or expired token
            MetaAdsPermissionError: Insufficient permissions
            MetaAdsValidationError: Invalid date range or entity ID
            MetaAdsClientError: Other API errors
        """
        try:
            logger.info(
                f"[META_CLIENT] Fetching insights for {entity_id}: "
                f"{start_date} to {end_date}, level={level}"
            )
            
            # Determine entity type and create appropriate object
            if level == "account":
                entity = AdAccount(entity_id)
            elif level == "campaign":
                entity = Campaign(entity_id)
            elif level == "adset":
                entity = AdSet(entity_id)
            else:  # ad
                entity = Ad(entity_id)
            
            # Fetch insights
            params = {
                'level': level,
                'time_range': {
                    'since': start_date,
                    'until': end_date
                },
                'time_increment': time_increment,
            }
            
            insights = entity.get_insights(
                fields=[
                    AdsInsights.Field.date_start,
                    AdsInsights.Field.date_stop,
                    AdsInsights.Field.spend,
                    AdsInsights.Field.impressions,
                    AdsInsights.Field.clicks,
                    AdsInsights.Field.actions,
                    AdsInsights.Field.action_values,
                ],
                params=params
            )
            
            result = []
            for insight in insights:
                result.append(dict(insight))
            
            logger.info(f"[META_CLIENT] Fetched {len(result)} insight records")
            return result
            
        except FacebookRequestError as e:
            return self._handle_api_error(e, f"fetching insights for {entity_id}")
    
    def _handle_api_error(self, error: FacebookRequestError, context: str) -> None:
        """Handle Facebook API errors with specific exceptions.
        
        WHAT:
            Translates FacebookRequestError into specific exception types.
            Logs error details for debugging.
        
        WHY:
            Allows calling code to handle different error types appropriately.
            Centralizes error logging and handling logic.
        
        Args:
            error: The Facebook API error
            context: Description of what operation failed
            
        Raises:
            MetaAdsAuthenticationError: For 401 errors
            MetaAdsPermissionError: For 403 errors
            MetaAdsValidationError: For 400 errors
            MetaAdsClientError: For other errors (429, 500, etc.)
        """
        error_code = error.api_error_code()
        error_message = error.api_error_message()
        http_status = error.http_status()
        
        logger.error(
            f"[META_CLIENT] API error while {context}: "
            f"HTTP {http_status}, Code {error_code}, Message: {error_message}"
        )
        
        # Map HTTP status to specific exceptions
        if http_status == 401:
            raise MetaAdsAuthenticationError(
                f"Authentication failed while {context}. Token may be expired or invalid."
            )
        elif http_status == 403:
            raise MetaAdsPermissionError(
                f"Permission denied while {context}. Check token permissions."
            )
        elif http_status == 400:
            raise MetaAdsValidationError(
                f"Invalid request while {context}: {error_message}"
            )
        elif http_status == 429:
            # Rate limit hit (should be prevented by decorator, but handle gracefully)
            raise MetaAdsClientError(
                f"Rate limit exceeded while {context}. This should not happen with rate limiting."
            )
        else:
            # 500, 503, or other server errors
            raise MetaAdsClientError(
                f"API error while {context}: HTTP {http_status}, {error_message}"
            )

