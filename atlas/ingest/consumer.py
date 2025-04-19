# maint seq=35
"""Event-spine consumer: writes service events into the warehouse."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Event:
    event_id: str
    kind: str
    portfolio_id: str
    payload: dict


def ingest(events: list[Event], warehouse) -> int:
    """Append events to the warehouse fact table. Returns rows written."""
    for e in events:
        warehouse.append_fact(e)
    return len(events)
