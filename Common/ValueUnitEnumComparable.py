from enum import Enum
from functools import total_ordering
from typing import TYPE_CHECKING, Any, Callable

class OrderedEnum(Enum):
    def __hash__(self):
        return super().__hash__()

    if TYPE_CHECKING:
        def __eq__(self, other: Any) -> bool: ...
        def __nq__(self, other: Any) -> bool: ...
        def __gt__(self, other: Any) -> bool: ...
        def __ge__(self, other: Any) -> bool: ...
        def __lt__(self, other: Any) -> bool: ...
        def __le__(self, other: Any) -> bool: ...

def OrderedEnumComparable[TEnum : OrderedEnum](
    get_order : Callable[[type[TEnum]], dict[TEnum, int]],
):
    def decorator(
        cls : type[TEnum],
    ) -> type[TEnum]:
        def __eq__(
            self : TEnum,
            other : Any,
        ) -> bool:
            if isinstance(other, cls):
                return self.name == other.name
            return NotImplemented

        def __gt__(
            self : TEnum,
            other : Any,
        ) -> bool:
            if isinstance(other, cls):
                order = get_order(cls)
                return order[self] > order[other]
            return NotImplemented

        cls.__eq__ = __eq__
        cls.__gt__ = __gt__

        return total_ordering(cls)

    return decorator
