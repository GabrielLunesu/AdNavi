from __future__ import annotations
from typing import Dict, Any, Optional
from datetime import date, timedelta
import re

class DateRangeParser:
    """
    Parses date-related phrases from natural language questions into structured date ranges.
    This is a simplified, pattern-based approach, not a full RAG system.
    """

    def __init__(self):
        # More specific patterns first
        self.patterns = {
            "last_week": r"last week",
            "this_week": r"this week",
            "last_month": r"last month",
            "this_month": r"this month",
            "yesterday": r"yesterday",
            "today": r"today",
            "in_september": r"in september",
        }

    def parse(self, question: str) -> Optional[Dict[str, Any]]:
        """
        Parses a question to find a date range.
        Returns a dictionary with 'start', 'end' or 'last_n_days'.
        """
        question_lower = question.lower()
        
        for key, pattern in self.patterns.items():
            if re.search(pattern, question_lower):
                return self._get_date_range_for_key(key)
        
        return None

    def _get_date_range_for_key(self, key: str) -> Dict[str, Any]:
        """
        Returns the corresponding date range for a matched key.
        """
        today = date.today()
        if key == "last_week":
            return {"last_n_days": 7}
        elif key == "this_week":
            start_of_week = today - timedelta(days=today.weekday())
            return {"start": start_of_week, "end": today}
        elif key == "last_month":
            return {"last_n_days": 30}
        elif key == "this_month":
            first_day_of_month = today.replace(day=1)
            return {"start": first_day_of_month, "end": today}
        elif key == "yesterday":
            return {"last_n_days": 1} # Special handling in translator
        elif key == "today":
            return {"last_n_days": 1} # Special handling in translator
        elif key == "in_september":
            # Assuming current year for simplicity. A more robust solution would handle year context.
            return {"start": date(today.year, 9, 1), "end": date(today.year, 9, 30)}
        
        return {}
