import pytest
from datetime import date, timedelta
from app.dsl.date_parser import DateRangeParser

@pytest.fixture
def parser():
    return DateRangeParser()

def test_parse_last_week(parser):
    result = parser.parse("What was my revenue last week?")
    assert result == {"last_n_days": 7}

def test_parse_this_week(parser):
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    result = parser.parse("Show me spend for this week")
    assert result == {"start": start_of_week, "end": today}

def test_parse_last_month(parser):
    result = parser.parse("How many conversions last month?")
    assert result == {"last_n_days": 30}

def test_parse_this_month(parser):
    today = date.today()
    first_day_of_month = today.replace(day=1)
    result = parser.parse("What's my ROAS this month?")
    assert result == {"start": first_day_of_month, "end": today}

def test_parse_yesterday(parser):
    result = parser.parse("How much did I spend yesterday?")
    assert result == {"last_n_days": 1}

def test_parse_today(parser):
    result = parser.parse("What's my CPC today?")
    assert result == {"last_n_days": 1}

def test_parse_in_september(parser):
    today = date.today()
    result = parser.parse("What was the spend in September?")
    assert result == {"start": date(today.year, 9, 1), "end": date(today.year, 9, 30)}

def test_no_date_phrase(parser):
    result = parser.parse("What is my ROAS?")
    assert result is None

def test_case_insensitivity(parser):
    result = parser.parse("show me spend THIS WEEK")
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    assert result == {"start": start_of_week, "end": today}
