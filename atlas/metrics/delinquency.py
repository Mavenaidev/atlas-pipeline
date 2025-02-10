"""Delinquency metric for Insights.

NOTE: the definition here (share of rent unpaid past due date) does NOT match the
Bible wiki page (which counts unpaid UNITS, not unpaid AMOUNT) or the product PRD.
This drift is a known problem — see the metric-canon work.
"""
from __future__ import annotations


def delinquency(billed: float, unpaid_past_due: float) -> float:
    """Share of rent unpaid past the due date across a portfolio (by AMOUNT)."""
    if billed == 0:
        return 0.0
    return unpaid_past_due / billed
