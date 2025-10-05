"""
Unit Tests for Metric Formatters
=================================

Tests the single source of truth for metric display formatting.

WHY these tests matter:
- Formatters are used by AnswerBuilder (GPT) and QAService fallback
- Bugs here would affect ALL answers (e.g., CPC showing "$0" instead of "$0.48")
- Need to verify currency, ratio, percentage, and count formatting
- Need to verify None handling (returns "N/A")

Coverage:
- Currency metrics: spend, revenue, cpa, cpl, cpi, cpp, cpc, cpm, aov, arpv
- Ratio metrics: roas, poas
- Percentage metrics: ctr, cvr
- Count metrics: clicks, impressions, conversions, leads, installs, purchases, visitors
- Edge cases: None values, zero values, very small values, very large values

Related:
- app/answer/formatters.py: Module being tested
- app/answer/answer_builder.py: Uses these formatters
- app/services/qa_service.py: Uses these formatters
"""

import pytest
from app.answer.formatters import (
    format_metric_value,
    format_delta_pct,
    fmt_currency,
    fmt_ratio_x,
    fmt_percent,
    fmt_count,
    get_metric_format_type,
)


# =====================================================================
# TEST CURRENCY FORMATTING
# =====================================================================

class TestCurrencyFormatting:
    """Test currency metrics: $, 2 decimals, thousands separators."""
    
    def test_cpc_format(self):
        """CPC should format as currency with 2 decimals."""
        # WHY this test: CPC values are often < $1, easy to round to "$0"
        assert format_metric_value("cpc", 0.4794) == "$0.48"
        assert format_metric_value("cpc", 0.01) == "$0.01"
        assert format_metric_value("cpc", 1.5) == "$1.50"
    
    def test_cpm_format(self):
        """CPM should format as currency with 2 decimals."""
        assert format_metric_value("cpm", 5.25) == "$5.25"
        assert format_metric_value("cpm", 12.50) == "$12.50"
    
    def test_cpl_format(self):
        """CPL should format as currency."""
        assert format_metric_value("cpl", 15.75) == "$15.75"
    
    def test_cpi_format(self):
        """CPI should format as currency."""
        assert format_metric_value("cpi", 2.99) == "$2.99"
    
    def test_cpp_format(self):
        """CPP should format as currency."""
        assert format_metric_value("cpp", 25.00) == "$25.00"
    
    def test_cpa_format(self):
        """CPA should format as currency."""
        assert format_metric_value("cpa", 18.45) == "$18.45"
    
    def test_aov_format(self):
        """AOV should format as currency."""
        assert format_metric_value("aov", 125.99) == "$125.99"
    
    def test_arpv_format(self):
        """ARPV should format as currency."""
        assert format_metric_value("arpv", 3.50) == "$3.50"
    
    def test_spend_format(self):
        """Spend should format as currency with thousands separators."""
        assert format_metric_value("spend", 1234.56) == "$1,234.56"
        assert format_metric_value("spend", 1000000.00) == "$1,000,000.00"
    
    def test_revenue_format(self):
        """Revenue should format as currency with thousands separators."""
        assert format_metric_value("revenue", 5432.10) == "$5,432.10"
    
    def test_profit_format(self):
        """Profit should format as currency with thousands separators."""
        assert format_metric_value("profit", 2500.75) == "$2,500.75"
    
    def test_currency_none_handling(self):
        """Currency metrics should return 'N/A' for None values."""
        assert format_metric_value("cpc", None) == "N/A"
        assert format_metric_value("spend", None) == "N/A"
    
    def test_currency_zero_handling(self):
        """Currency metrics should format zero as $0.00."""
        assert format_metric_value("cpc", 0) == "$0.00"
        assert format_metric_value("spend", 0) == "$0.00"


# =====================================================================
# TEST RATIO FORMATTING
# =====================================================================

class TestRatioFormatting:
    """Test ratio metrics: × symbol, 2 decimals."""
    
    def test_roas_format(self):
        """ROAS should format as ratio with × symbol."""
        # WHY: ROAS = revenue / spend, shows return multiple
        assert format_metric_value("roas", 2.456) == "2.46×"
        assert format_metric_value("roas", 0.85) == "0.85×"  # Below 1 = losing money
        assert format_metric_value("roas", 10.5) == "10.50×"
    
    def test_poas_format(self):
        """POAS should format as ratio with × symbol."""
        assert format_metric_value("poas", 1.75) == "1.75×"
        assert format_metric_value("poas", 0.5) == "0.50×"
    
    def test_ratio_none_handling(self):
        """Ratio metrics should return 'N/A' for None values."""
        assert format_metric_value("roas", None) == "N/A"
        assert format_metric_value("poas", None) == "N/A"
    
    def test_ratio_zero_handling(self):
        """Ratio metrics should format zero as 0.00×."""
        assert format_metric_value("roas", 0) == "0.00×"


# =====================================================================
# TEST PERCENTAGE FORMATTING
# =====================================================================

class TestPercentageFormatting:
    """Test percentage metrics: %, 1 decimal, input is decimal."""
    
    def test_ctr_format(self):
        """CTR should format as percentage (input is decimal fraction)."""
        # WHY: CTR is stored as decimal (0.042 = 4.2%)
        assert format_metric_value("ctr", 0.042) == "4.2%"
        assert format_metric_value("ctr", 0.157) == "15.7%"
        assert format_metric_value("ctr", 0.005) == "0.5%"
    
    def test_cvr_format(self):
        """CVR should format as percentage (input is decimal fraction)."""
        assert format_metric_value("cvr", 0.025) == "2.5%"
        assert format_metric_value("cvr", 0.108) == "10.8%"
    
    def test_percentage_none_handling(self):
        """Percentage metrics should return 'N/A' for None values."""
        assert format_metric_value("ctr", None) == "N/A"
        assert format_metric_value("cvr", None) == "N/A"
    
    def test_percentage_zero_handling(self):
        """Percentage metrics should format zero as 0.0%."""
        assert format_metric_value("ctr", 0) == "0.0%"


# =====================================================================
# TEST COUNT FORMATTING
# =====================================================================

class TestCountFormatting:
    """Test count metrics: whole numbers, thousands separators."""
    
    def test_clicks_format(self):
        """Clicks should format as whole number with thousands separators."""
        assert format_metric_value("clicks", 1234) == "1,234"
        assert format_metric_value("clicks", 1000000) == "1,000,000"
    
    def test_impressions_format(self):
        """Impressions should format as whole number with thousands separators."""
        assert format_metric_value("impressions", 50000) == "50,000"
    
    def test_conversions_format(self):
        """Conversions should format as whole number."""
        # NOTE: Conversions can be decimal in DB, but displayed as whole number
        assert format_metric_value("conversions", 125) == "125"
        assert format_metric_value("conversions", 125.8) == "126"  # Rounds
    
    def test_leads_format(self):
        """Leads should format as whole number."""
        assert format_metric_value("leads", 45) == "45"
    
    def test_installs_format(self):
        """Installs should format as whole number."""
        assert format_metric_value("installs", 789) == "789"
    
    def test_purchases_format(self):
        """Purchases should format as whole number."""
        assert format_metric_value("purchases", 234) == "234"
    
    def test_visitors_format(self):
        """Visitors should format as whole number."""
        assert format_metric_value("visitors", 5432) == "5,432"
    
    def test_count_none_handling(self):
        """Count metrics should return 'N/A' for None values."""
        assert format_metric_value("clicks", None) == "N/A"
        assert format_metric_value("impressions", None) == "N/A"
    
    def test_count_zero_handling(self):
        """Count metrics should format zero as 0."""
        assert format_metric_value("clicks", 0) == "0"


# =====================================================================
# TEST DELTA PERCENTAGE FORMATTING
# =====================================================================

class TestDeltaPercentageFormatting:
    """Test period-over-period change formatting."""
    
    def test_positive_delta(self):
        """Positive changes should include + sign."""
        # WHY: Makes it clear the metric increased
        assert format_delta_pct(0.19) == "+19.0%"
        assert format_delta_pct(0.055) == "+5.5%"
    
    def test_negative_delta(self):
        """Negative changes should include - sign."""
        assert format_delta_pct(-0.15) == "-15.0%"
        assert format_delta_pct(-0.025) == "-2.5%"
    
    def test_zero_delta(self):
        """Zero change should show +0.0%."""
        assert format_delta_pct(0) == "+0.0%"
    
    def test_delta_none_handling(self):
        """Delta should return 'N/A' for None values."""
        assert format_delta_pct(None) == "N/A"


# =====================================================================
# TEST EDGE CASES
# =====================================================================

class TestEdgeCases:
    """Test edge cases and boundary conditions."""
    
    def test_unknown_metric_fallback(self):
        """Unknown metrics should fall back to 2-decimal float."""
        assert format_metric_value("unknown_metric", 123.456) == "123.46"
    
    def test_unknown_metric_none(self):
        """Unknown metrics should return 'N/A' for None."""
        assert format_metric_value("unknown_metric", None) == "N/A"
    
    def test_case_insensitive_metric_names(self):
        """Metric names should be case-insensitive."""
        assert format_metric_value("CPC", 0.50) == "$0.50"
        assert format_metric_value("Roas", 2.5) == "2.50×"
        assert format_metric_value("CTR", 0.05) == "5.0%"
    
    def test_very_small_values(self):
        """Very small values should format correctly."""
        assert format_metric_value("cpc", 0.001) == "$0.00"  # Rounds to 2 decimals
        assert format_metric_value("ctr", 0.001) == "0.1%"
    
    def test_very_large_values(self):
        """Very large values should format with thousands separators."""
        assert format_metric_value("spend", 1234567.89) == "$1,234,567.89"
        assert format_metric_value("impressions", 10000000) == "10,000,000"


# =====================================================================
# TEST FORMAT TYPE DETECTION
# =====================================================================

class TestFormatTypeDetection:
    """Test the get_metric_format_type helper function."""
    
    def test_currency_metrics(self):
        """Currency metrics should be detected correctly."""
        assert get_metric_format_type("cpc") == "currency"
        assert get_metric_format_type("spend") == "currency"
        assert get_metric_format_type("revenue") == "currency"
    
    def test_ratio_metrics(self):
        """Ratio metrics should be detected correctly."""
        assert get_metric_format_type("roas") == "ratio"
        assert get_metric_format_type("poas") == "ratio"
    
    def test_percentage_metrics(self):
        """Percentage metrics should be detected correctly."""
        assert get_metric_format_type("ctr") == "percentage"
        assert get_metric_format_type("cvr") == "percentage"
    
    def test_count_metrics(self):
        """Count metrics should be detected correctly."""
        assert get_metric_format_type("clicks") == "count"
        assert get_metric_format_type("impressions") == "count"
    
    def test_unknown_metric(self):
        """Unknown metrics should return 'float'."""
        assert get_metric_format_type("unknown") == "float"


# =====================================================================
# TEST LOW-LEVEL FORMATTERS
# =====================================================================

class TestLowLevelFormatters:
    """Test the individual formatting functions directly."""
    
    def test_fmt_currency(self):
        """Test currency formatter directly."""
        assert fmt_currency(1234.56) == "$1,234.56"
        assert fmt_currency(0.99) == "$0.99"
        assert fmt_currency(None) == "N/A"
        assert fmt_currency(100, "€") == "€100.00"
    
    def test_fmt_ratio_x(self):
        """Test ratio formatter directly."""
        assert fmt_ratio_x(2.5) == "2.50×"
        assert fmt_ratio_x(0.5) == "0.50×"
        assert fmt_ratio_x(None) == "N/A"
    
    def test_fmt_percent(self):
        """Test percentage formatter directly."""
        assert fmt_percent(0.05) == "5.0%"
        assert fmt_percent(0.157) == "15.7%"
        assert fmt_percent(None) == "N/A"
    
    def test_fmt_count(self):
        """Test count formatter directly."""
        assert fmt_count(1234) == "1,234"
        assert fmt_count(1234.9) == "1,235"  # Rounds
        assert fmt_count(None) == "N/A"


# =====================================================================
# INTEGRATION TESTS
# =====================================================================

class TestIntegration:
    """Test formatters with realistic scenarios."""
    
    def test_dashboard_kpi_formatting(self):
        """Test typical dashboard KPI values."""
        # Scenario: Dashboard shows 4 KPIs
        kpis = {
            "spend": 12500.75,
            "revenue": 45678.90,
            "roas": 3.65,
            "ctr": 0.0425,
        }
        
        expected = {
            "spend": "$12,500.75",
            "revenue": "$45,678.90",
            "roas": "3.65×",
            "ctr": "4.2%",
        }
        
        for metric, value in kpis.items():
            assert format_metric_value(metric, value) == expected[metric]
    
    def test_qa_answer_formatting(self):
        """Test values as they would appear in QA answers."""
        # Scenario: User asks "What was my CPC last week?"
        assert format_metric_value("cpc", 0.4794) == "$0.48"
        
        # Scenario: User asks "What's my ROAS?"
        assert format_metric_value("roas", 2.456789) == "2.46×"
        
        # Scenario: User asks "How many clicks did I get?"
        assert format_metric_value("clicks", 125678) == "125,678"
    
    def test_breakdown_formatting(self):
        """Test formatting breakdown values (top performers)."""
        # Scenario: Top campaigns by CPC
        campaigns = [
            {"name": "Campaign A", "cpc": 0.35},
            {"name": "Campaign B", "cpc": 0.52},
            {"name": "Campaign C", "cpc": 0.89},
        ]
        
        for campaign in campaigns:
            formatted = format_metric_value("cpc", campaign["cpc"])
            assert formatted.startswith("$")
            assert "." in formatted

