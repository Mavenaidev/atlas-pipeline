# Backfill runbook

1. Identify the window to replay (`window_start`, `window_end`).
2. **Truncate the affected fact partitions first.** (Easy to forget. Don't.)
3. Run `run_backfill(window_start, window_end, source, warehouse)`.
4. Spot-check Insights collections for an implausible jump.

> If collections numbers jump implausibly after a backfill, you almost certainly
> double-counted — you skipped step 2.
