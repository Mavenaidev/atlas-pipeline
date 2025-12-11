from atlas.backfill.backfill import run_backfill


class FakeWarehouse:
    def __init__(self):
        self.facts = {}
        self.watermark = None
    def existing_event_ids(self, ids):
        return {i for i in ids if i in self.facts}
    def append_fact(self, e):
        self.facts[e.event_id] = e
    def set_watermark(self, w):
        self.watermark = w


class FakeSource:
    def __init__(self, events):
        self._events = events
    def read_events(self, a, b):
        return self._events


def test_replay_is_idempotent():
    from atlas.ingest.consumer import Event
    evs = [Event('e1', 'payment', 'p1', {}), Event('e2', 'payment', 'p1', {})]
    wh = FakeWarehouse()
    src = FakeSource(evs)
    assert run_backfill('a', 'b', src, wh) == 2
    # replay the same window: must write zero, not double-count
    assert run_backfill('a', 'b', src, wh) == 0
