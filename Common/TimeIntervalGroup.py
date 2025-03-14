from .TimeInterval import TimeInterval

class TimeIntervalGroup:
    def __init__(
        self,
        intervals : tuple[TimeInterval, ...]
    ):
        self.intervals = sorted(intervals, key = lambda interval: (interval.unit.value, interval.value))

    def __str__(
        self,
    ):
        return " ".join((str(interval) for interval in self.intervals))
