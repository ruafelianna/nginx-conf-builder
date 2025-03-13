from abc import ABC
from typing import Callable

from Contexts import MainContext
from Directives import DirectiveBase
from Types import DirectiveDict

class GeneratorBase(ABC):
    def __init__(
        self,
        to_str : Callable[[tuple[DirectiveDict, ...]], str],
    ):
        self.to_str = to_str

    def build(
        self,
        directive : DirectiveBase,
    ) -> str:
        ctx : DirectiveDict = directive.build()

        if isinstance(directive, MainContext):
            if "block" in ctx:
                return self.to_str(ctx["block"])
            else:
                raise ValueError("Main context doesn't have any content")
        else:
            return self.to_str((ctx,))

    def build_many(
        self,
        directives : tuple[DirectiveBase, ...],
    ) -> str:
        return self.to_str(tuple((d.build() for d in directives)))
