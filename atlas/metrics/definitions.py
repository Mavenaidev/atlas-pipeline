"""Canonical Insights metric definitions (ADR-018, Accepted 2026-02-18).

This module is the SINGLE SOURCE OF TRUTH for how Insights metrics are defined.
It supersedes the metric descriptions in the Bible wiki (now marked stale) and the
product PRD where they disagreed. If a dashboard, a doc, or a sales deck states a
metric differently from here, this module wins. Each definition is code-as-doc:
the docstring IS the canonical definition.
"""
from __future__ import annotations

from atlas.metrics.collections import collections_rate
from atlas.metrics.delinquency import delinquency
from atlas.metrics.turn_time import turn_time_days

CANONICAL = {
    "collections_rate": {
        "definition": "Percent of BILLED rent successfully COLLECTED within the period.",
        "basis": "amount",
        "fn": collections_rate,
    },
    "delinquency": {
        "definition": "Share of BILLED rent unpaid past the due date, by AMOUNT "
                      "(NOT by unit count — that was the stale Bible definition).",
        "basis": "amount",
        "fn": delinquency,
    },
    "turn_time_days": {
        "definition": "Median days a unit sits vacant between residents.",
        "basis": "median_days",
        "fn": turn_time_days,
    },
}
