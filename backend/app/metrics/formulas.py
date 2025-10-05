"""
Metric Formulas
===============

Pure mathematical functions for computing derived metrics from base measures.

SINGLE SOURCE OF TRUTH for all metric calculations.

Base measures (stored in MetricFact):
- spend, impressions, clicks, conversions, revenue
- leads, installs, purchases, visitors, profit

Derived metrics (computed on-demand):
- Efficiency/Cost: cpc, cpm, cpl, cpi, cpp
- Revenue/Value: roas, poas, arpv, aov, cpa
- Performance/Engagement: ctr, cvr

All formulas include divide-by-zero guards and return None when computation is impossible.

Used by:
- app/metrics/registry.py: Maps metric names to these functions
- app/dsl/executor.py: Computes metrics for ad-hoc queries
- app/services/compute_service.py: Computes metrics for Pnl snapshots

Design principles:
- Pure functions: no side effects, deterministic
- Type hints: clear input/output contracts
- Guards: return None instead of raising exceptions
- Comments: explain WHY each metric matters
"""

from typing import Optional


def safe_div(numerator: Optional[float], denominator: Optional[float]) -> Optional[float]:
    """
    Safely divide two numbers with divide-by-zero guard.
    
    Args:
        numerator: Top of fraction (can be None)
        denominator: Bottom of fraction (can be None)
        
    Returns:
        numerator / denominator if denominator > 0, else None
        
    Examples:
        >>> safe_div(100, 50)
        2.0
        
        >>> safe_div(100, 0)
        None
        
        >>> safe_div(None, 50)
        None
        
        >>> safe_div(100, -10)
        -10.0  # Negative denominators are allowed (though rare in ad metrics)
    """
    if numerator is None or denominator is None:
        return None
    if denominator <= 0:
        return None
    return numerator / denominator


# =====================================================================
# EFFICIENCY / COST METRICS
# =====================================================================

def cpc(spend: Optional[float], clicks: Optional[float]) -> Optional[float]:
    """
    Cost Per Click (CPC).
    
    Formula: spend / clicks
    
    WHY: Measures how much you pay per click. Lower is better for efficiency.
    Lower CPC → getting more traffic for your budget.
    
    Examples:
        >>> cpc(1000, 500)  # $1000 / 500 clicks
        2.0  # $2 per click
        
        >>> cpc(1000, 0)  # No clicks
        None
    """
    return safe_div(spend, clicks)


def cpm(spend: Optional[float], impressions: Optional[float]) -> Optional[float]:
    """
    Cost Per Mille (CPM) - cost per 1000 impressions.
    
    Formula: (spend / impressions) * 1000
    
    WHY: Standard metric for awareness campaigns. Measures cost to reach 1000 people.
    Lower CPM → more efficient reach.
    
    Examples:
        >>> cpm(100, 50000)  # $100 / 50k impressions
        2.0  # $2 per 1000 impressions
        
        >>> cpm(100, 0)  # No impressions
        None
    """
    result = safe_div(spend, impressions)
    return (result * 1000) if result is not None else None


def cpl(spend: Optional[float], leads: Optional[float]) -> Optional[float]:
    """
    Cost Per Lead (CPL).
    
    Formula: spend / leads
    
    WHY: Measures efficiency of lead generation campaigns.
    Critical for B2B and lead-gen advertisers.
    
    Examples:
        >>> cpl(1000, 50)  # $1000 / 50 leads
        20.0  # $20 per lead
    """
    return safe_div(spend, leads)


def cpi(spend: Optional[float], installs: Optional[float]) -> Optional[float]:
    """
    Cost Per Install (CPI).
    
    Formula: spend / installs
    
    WHY: Key metric for mobile app campaigns (App Install objective).
    Measures cost to acquire one app installation.
    
    Examples:
        >>> cpi(5000, 1000)  # $5000 / 1000 installs
        5.0  # $5 per install
    """
    return safe_div(spend, installs)


def cpp(spend: Optional[float], purchases: Optional[float]) -> Optional[float]:
    """
    Cost Per Purchase (CPP).
    
    Formula: spend / purchases
    
    WHY: Direct measure of ecommerce campaign efficiency.
    Similar to CPA but specifically for purchase conversions.
    
    Examples:
        >>> cpp(2000, 100)  # $2000 / 100 purchases
        20.0  # $20 per purchase
    """
    return safe_div(spend, purchases)


def cpa(spend: Optional[float], conversions: Optional[float]) -> Optional[float]:
    """
    Cost Per Acquisition (CPA) - generic conversion cost.
    
    Formula: spend / conversions
    
    WHY: Most common efficiency metric. Measures cost per conversion action
    (can be purchase, signup, download, etc. depending on campaign objective).
    
    Examples:
        >>> cpa(1000, 50)  # $1000 / 50 conversions
        20.0  # $20 per conversion
    """
    return safe_div(spend, conversions)


# =====================================================================
# REVENUE / VALUE METRICS
# =====================================================================

def roas(revenue: Optional[float], spend: Optional[float]) -> Optional[float]:
    """
    Return on Ad Spend (ROAS).
    
    Formula: revenue / spend
    
    WHY: THE key profitability metric. Shows revenue multiple per dollar spent.
    ROAS of 2.5 → every $1 spent returns $2.50 in revenue.
    
    Targets vary by industry:
    - Ecommerce: 4-5x ROAS is good
    - SaaS: 3x+ ROAS acceptable (long customer lifetime value)
    - Lead gen: Depends on lead value and close rate
    
    Examples:
        >>> roas(5000, 1000)  # $5k revenue / $1k spend
        5.0  # 5x ROAS - excellent
        
        >>> roas(800, 1000)  # $800 revenue / $1k spend
        0.8  # 0.8x ROAS - losing money
    """
    return safe_div(revenue, spend)


def poas(profit: Optional[float], spend: Optional[float]) -> Optional[float]:
    """
    Profit on Ad Spend (POAS).
    
    Formula: profit / spend
    
    WHY: More accurate than ROAS because it accounts for costs (COGS, fulfillment).
    profit = revenue - costs
    
    POAS of 2.0 → every $1 spent returns $2 in PROFIT (not just revenue).
    
    Note: Requires profit tracking (revenue - COGS/costs).
    
    Examples:
        >>> poas(3000, 1000)  # $3k profit / $1k spend
        3.0  # 3x POAS
        
        >>> poas(-500, 1000)  # Lost money
        -0.5  # Negative POAS
    """
    return safe_div(profit, spend)


def arpv(revenue: Optional[float], visitors: Optional[float]) -> Optional[float]:
    """
    Average Revenue Per Visitor (ARPV).
    
    Formula: revenue / visitors
    
    WHY: Measures revenue efficiency of traffic (landing page performance).
    Higher ARPV → better conversion funnel or higher AOV.
    
    Examples:
        >>> arpv(10000, 5000)  # $10k revenue / 5k visitors
        2.0  # $2 per visitor
    """
    return safe_div(revenue, visitors)


def aov(revenue: Optional[float], conversions: Optional[float]) -> Optional[float]:
    """
    Average Order Value (AOV).
    
    Formula: revenue / conversions
    
    WHY: Measures average transaction size. Key for ecommerce optimization.
    Increasing AOV (upsells, bundles) → more revenue per customer.
    
    Examples:
        >>> aov(50000, 500)  # $50k revenue / 500 purchases
        100.0  # $100 average order
    """
    return safe_div(revenue, conversions)


# =====================================================================
# PERFORMANCE / ENGAGEMENT METRICS
# =====================================================================

def ctr(clicks: Optional[float], impressions: Optional[float]) -> Optional[float]:
    """
    Click-Through Rate (CTR).
    
    Formula: clicks / impressions
    
    WHY: Measures ad creative effectiveness. How many people who see your ad click it?
    Higher CTR → more engaging ad creative.
    
    Typical values:
    - Search ads: 2-5% CTR
    - Display ads: 0.5-1% CTR
    - Social ads: 1-3% CTR
    
    Note: Returns decimal (0.05 = 5% CTR). Frontend should format as percentage.
    
    Examples:
        >>> ctr(500, 10000)  # 500 clicks / 10k impressions
        0.05  # 5% CTR
    """
    return safe_div(clicks, impressions)


def cvr(conversions: Optional[float], clicks: Optional[float]) -> Optional[float]:
    """
    Conversion Rate (CVR).
    
    Formula: conversions / clicks
    
    WHY: Measures landing page + offer effectiveness. How many clickers convert?
    Higher CVR → better landing page or offer.
    
    Typical values:
    - Ecommerce: 2-5% CVR
    - Lead gen: 10-20% CVR (form submissions)
    - SaaS trials: 5-15% CVR
    
    Note: Returns decimal (0.03 = 3% CVR). Frontend should format as percentage.
    
    Examples:
        >>> cvr(50, 1000)  # 50 conversions / 1000 clicks
        0.05  # 5% CVR
    """
    return safe_div(conversions, clicks)


# =====================================================================
# REGISTRY EXPORT
# =====================================================================

# Map function names to actual functions for registry lookup
ALL_FORMULAS = {
    "cpc": cpc,
    "cpm": cpm,
    "cpl": cpl,
    "cpi": cpi,
    "cpp": cpp,
    "cpa": cpa,
    "roas": roas,
    "poas": poas,
    "arpv": arpv,
    "aov": aov,
    "ctr": ctr,
    "cvr": cvr,
}

