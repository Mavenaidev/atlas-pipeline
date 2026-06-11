"""Backfill: replay historical event-spine events to rebuild metrics.

IDEMPOTENT as of PLT-192 (Dec 2025): replaying the same window no longer
double-counts. We dedupe by event_id against the warehouse and track a watermark
so a re-run is a no-op for already-ingested events. This is the fix for the SEV-3
where a backfill from the stale runbook inflated Insights collections/delinquency.
"""
from __future__ import annotations

from atlas.ingest.consumer import ingest


def run_backfill(window_start: str, window_end: str, source, warehouse) -> int:
    events = source.read_events(window_start, window_end)
    # IDEMPOTENCY: drop any event whose event_id is already a fact. The warehouse
    # fact table is keyed by event_id, so a replay of an overlapping window is safe.
    existing = warehouse.existing_event_ids([e.event_id for e in events])
    fresh = [e for e in events if e.event_id not in existing]
    written = ingest(fresh, warehouse)
    warehouse.set_watermark(window_end)
    return written
