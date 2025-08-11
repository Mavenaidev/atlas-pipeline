# maint seq=94
from atlas.metrics.collections import collections_rate
from atlas.metrics.turn_time import turn_time_days


def test_collections_zero_billed():
    assert collections_rate(0, 0) == 0.0


def test_turn_time_median():
    assert turn_time_days([1, 3, 5]) == 3.0
