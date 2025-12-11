# Backfill runbook (updated PLT-192)

1. Identify the window to replay (`window_start`, `window_end`).
2. Run `run_backfill(window_start, window_end, source, warehouse)`.

> You no longer need to truncate first. The backfill is **idempotent**: it dedupes by
> `event_id`, so replaying an overlapping window is a no-op for already-ingested events.
> The old 'truncate first' step is exactly what got missed in the Dec 2025 incident.
