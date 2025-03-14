from abc import ABC
from typing import Self

from .DirectiveDict import DirectiveDict

class DirectiveBase(ABC):
    def __init__(
        self,
        name : str,
        args : tuple[str, ...] = (),
        block : tuple[Self | None, ...] = (),
    ):
        self.name = name
        self.args = args
        self.block = block

    def build(
        self,
    ) -> DirectiveDict:
        result : DirectiveDict = {
            "directive": self.name,
            "args": self.args,
        }

        if len(self.block) > 0:
            result["block"] = tuple((b.build() for b in self.block if b))

        return result
