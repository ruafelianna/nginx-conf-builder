from enum import Enum
from functools import total_ordering
from typing import Any

@total_ordering
class Enum_TimeIntervalUnit(Enum):
    milliseconds = "ms"
    seconds  = "s"
    minutes = "m"
    hours = "h"
    days = "d"
    weeks = "w"
    months = "M" # 30 days
    years = "y" # 365 days

    def __hash__(
        self,
    ) -> int:
        return super().__hash__()

    def __eq__(
        self,
        other : Any,
    ) -> bool:
        return (
            type(self) == type(other)
            and self.name == other.name
        ) \
        or NotImplemented

    def __gt__(
        self,
        other : Any,
    ) -> bool:
        return (
            type(self) == type(other)
            and _order[self] > _order[other]
        ) \
        or NotImplemented

_order : dict[Enum_TimeIntervalUnit, int] = {
    Enum_TimeIntervalUnit.milliseconds: 0,
    Enum_TimeIntervalUnit.seconds: 1,
    Enum_TimeIntervalUnit.minutes: 2,
    Enum_TimeIntervalUnit.hours: 3,
    Enum_TimeIntervalUnit.days: 4,
    Enum_TimeIntervalUnit.weeks: 5,
    Enum_TimeIntervalUnit.months: 6,
    Enum_TimeIntervalUnit.years: 7,
}
