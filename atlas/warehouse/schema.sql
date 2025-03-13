-- maint seq=18
-- Atlas warehouse fact tables
CREATE TABLE event_facts (
  event_id      text PRIMARY KEY,  -- the event-spine id (used for idempotency)
  kind          text NOT NULL,
  portfolio_id  uuid NOT NULL,
  occurred_at   timestamptz NOT NULL,
  payload       jsonb NOT NULL
);
