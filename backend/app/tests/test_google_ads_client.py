"""Unit tests for Google Ads client service.

WHAT:
    Validate GAQL helpers, mapping, and basic parsing without real SDK/network.

WHY:
    Ensure separation and single responsibility with testable behavior.

REFERENCES:
    app/services/google_ads_client.py
    docs/living-docs/GOOGLE_INTEGRATION_STATUS.MD
"""

from datetime import date

import types

from app.models import GoalEnum
from app.services.google_ads_client import GAdsClient, map_channel_to_goal


class _FakeService:
    def __init__(self, responses):
        self._responses = responses

    def search(self, customer_id, query, page_size=10000):  # noqa: ARG002
        # Return the pre-seeded response iterator
        return iter(self._responses.get(query, []))

    def search_stream(self, customer_id, query):  # noqa: ARG002
        # Return batches with `.results` to simulate streaming
        batch = types.SimpleNamespace(results=self._responses.get(query, []))
        return [batch]


class _FakeClient:
    def __init__(self, service):
        self._service = service

    def get_service(self, name):  # noqa: ARG002
        return self._service


def _mk_row(ns_dict):
    # Build a nested SimpleNamespace mock similar to SDK rows
    return types.SimpleNamespace(**ns_dict)


def test_map_channel_to_goal():
    assert map_channel_to_goal("SEARCH") == GoalEnum.conversions
    assert map_channel_to_goal("DISPLAY") == GoalEnum.awareness
    assert map_channel_to_goal("PERFORMANCE_MAX") == GoalEnum.purchases
    assert map_channel_to_goal("APP") == GoalEnum.app_installs
    assert map_channel_to_goal("UNKNOWN") == GoalEnum.other
    assert map_channel_to_goal(None) == GoalEnum.other


def test_list_campaigns_parses_fields():
    q = (
        "SELECT campaign.id, campaign.name, campaign.status, "
        "campaign.serving_status, campaign.primary_status, "
        "campaign.primary_status_reasons, campaign.advertising_channel_type "
        "FROM campaign ORDER BY campaign.name"
    )
    fake_row = _mk_row({
        "campaign": types.SimpleNamespace(
            id="123",
            name="Test Campaign",
            status="ENABLED",
            serving_status="SERVING",
            primary_status="ELIGIBLE",
            primary_status_reasons=["POLICY_APPROVED"],
            advertising_channel_type="SEARCH",
        )
    })
    fake_service = _FakeService({q: [fake_row]})
    client = GAdsClient(client=_FakeClient(fake_service))
    rows = client.list_campaigns("1111111111")
    assert rows and rows[0]["id"] == "123"
    assert rows[0]["primary_status"] == "ELIGIBLE"
    assert rows[0]["advertising_channel_type"] == "SEARCH"


def test_get_customer_metadata_returns_timezone_currency():
    q = "SELECT customer.time_zone, customer.currency_code FROM customer LIMIT 1"
    fake_row = _mk_row({
        "customer": types.SimpleNamespace(time_zone="Europe/Vienna", currency_code="USD")
    })
    client = GAdsClient(client=_FakeClient(_FakeService({q: [fake_row]})))
    meta = client.get_customer_metadata("2222222222")
    assert meta["time_zone"] == "Europe/Vienna"
    assert meta["currency_code"] == "USD"


def test_fetch_daily_metrics_normalizes_spend_and_fields():
    start = date(2024, 10, 1)
    end = date(2024, 10, 2)
    q = (
        f"SELECT campaign.id, campaign.name, "
        "metrics.impressions, metrics.clicks, metrics.cost_micros, "
        "metrics.conversions, metrics.conversions_value, segments.date "
        f"FROM campaign WHERE segments.date BETWEEN '{start.isoformat()}' AND '{end.isoformat()}'"
    )
    fake_row = _mk_row({
        "metrics": types.SimpleNamespace(
            impressions=100,
            clicks=10,
            cost_micros=1234567,
            conversions=2.0,
            conversions_value=50.0,
        ),
        "segments": types.SimpleNamespace(date=start),
    })
    client = GAdsClient(client=_FakeClient(_FakeService({q: [fake_row]})))
    data = client.fetch_daily_metrics("3333333333", start, end, level="campaign")
    assert data and data[0]["spend"] == 1.234567
    assert data[0]["clicks"] == 10
    assert data[0]["revenue"] == 50.0
    assert "resource_id" in data[0]
