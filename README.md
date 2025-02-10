# atlas-pipeline (Atlas)

Atlas ingests events from every Veremont service over the **event spine** into the
warehouse and powers **Insights**: collections, delinquency, turn-time, and
vendor-SLA dashboards.

## Layout

- `atlas/ingest/` — event-spine consumers writing to the warehouse
- `atlas/backfill/` — re-process historical events (the **backfill runbook** lives here)
- `atlas/metrics/` — Insights metric computations (collections, delinquency, turn-time)
- `atlas/warehouse/` — warehouse schema + loaders
- `tests/`

## Backfill

A backfill replays historical event-spine events to rebuild metrics. See
`atlas/backfill/runbook.md`. **It must be idempotent** — replaying the same events
must not change the result.
