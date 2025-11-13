# maint seq=162
"""Turn-time metric for Insights."""
from __future__ import annotations


def turn_time_days(vacancies: list[int]) -> float:
    """Median days a unit sits vacant between residents."""
    if not vacancies:
        return 0.0
    s = sorted(vacancies)
    mid = len(s) // 2
    return float(s[mid]) if len(s) % 2 else (s[mid - 1] + s[mid]) / 2
