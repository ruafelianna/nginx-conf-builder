from functools import total_ordering
from typing import Any

from .Enum_SizeUnit import Enum_SizeUnit

@total_ordering
class Size:
    def __init__(
        self,
        value : int,
        unit : Enum_SizeUnit = Enum_SizeUnit.bytes,
    ):
        self.value = value
        self.unit = unit

    def __str__(
        self,
    ):
        return f"{self.value}{self.unit.value}"

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
            and self.value == other.value
            and self.unit == other.unit
        ) \
        or NotImplemented

    def __gt__(
        self,
        other : Any,
    ) -> bool:
        return (
            type(self) == type(other)
            and (
                self.unit > other.unit
                or (
                    self.unit == other.unit
                    and self.value > other.value
                )
            )
        ) \
        or NotImplemented
