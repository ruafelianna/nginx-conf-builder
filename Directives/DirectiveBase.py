from __future__ import annotations

from abc import ABC

class DirectiveBase(ABC):
    def __init__(
        self,
        name : str,
        args : tuple[str] = (),
        block : tuple[DirectiveBase | None] = (),
    ):
        self.name = name
        self.args = args
        self.block = block

    def build(self):
        result = {
            "directive": self.name,
            "args": self.args,
        }

        if len(self.block) > 0:
            result["block"] = tuple((b.build() for b in self.block if b))

        return result
