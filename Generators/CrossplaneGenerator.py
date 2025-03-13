from crossplane import build as crossplane_build

from .GeneratorBase import GeneratorBase

class CrossplaneGenerator(GeneratorBase):
    def __init__(
        self,
    ):
        super().__init__(crossplane_build)
