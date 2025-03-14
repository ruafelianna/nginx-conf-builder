from enum import Enum
from functools import total_ordering
from typing import Any

@total_ordering
class Enum_SizeUnit(Enum):
    bytes = ""
    kilobytes = "k"
    megabytes = "m"
    gigabytes = "g"

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

_order : dict[Enum_SizeUnit, int] = {
    Enum_SizeUnit.bytes: 0,
    Enum_SizeUnit.kilobytes: 1,
    Enum_SizeUnit.megabytes: 2,
    Enum_SizeUnit.gigabytes: 3,
}
