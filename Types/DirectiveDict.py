from __future__ import annotations

from typing import NotRequired, TypedDict

class DirectiveDict(TypedDict):
    directive: str
    args: tuple[str, ...]
    block: NotRequired[tuple[DirectiveDict, ...]]
