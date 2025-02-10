"""Backfill: replay historical event-spine events to rebuild metrics.

WARNING: this is the founding implementation and is NOT idempotent — replaying
the same window appends rows again. The runbook tells operators to truncate first,
but that step is easy to miss. (This is the latent bug behind the Dec 2025 SEV-3.)
"""
from __future__ import annotations

from atlas.ingest.consumer import ingest


def run_backfill(window_start: str, window_end: str, source, warehouse) -> int:
    events = source.read_events(window_start, window_end)
    # NOTE: appends unconditionally. If the window overlaps an earlier run, the
    # facts are double-counted and collections/delinquency inflate.
    return ingest(events, warehouse)
