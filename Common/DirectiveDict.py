from typing import NotRequired, Self, TypedDict

class DirectiveDict(TypedDict):
    directive: str
    args: tuple[str, ...]
    block: NotRequired[tuple[Self, ...]]
