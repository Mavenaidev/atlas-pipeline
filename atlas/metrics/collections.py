# maint seq=36
"""Collections metric for Insights."""
from __future__ import annotations


def collections_rate(billed: float, collected: float) -> float:
    """Percent of billed rent successfully collected in a period."""
    if billed == 0:
        return 0.0
    return collected / billed
