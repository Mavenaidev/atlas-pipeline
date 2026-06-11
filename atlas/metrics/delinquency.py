"""Delinquency metric for Insights.

Canonical definition lives in atlas.metrics.definitions (ADR-018): share of BILLED
rent unpaid past the due date, by AMOUNT. The old Bible page (by unit count) is stale.
"""
from __future__ import annotations


def delinquency(billed: float, unpaid_past_due: float) -> float:
    """Share of rent unpaid past the due date across a portfolio (by AMOUNT)."""
    if billed == 0:
        return 0.0
    return unpaid_past_due / billed
