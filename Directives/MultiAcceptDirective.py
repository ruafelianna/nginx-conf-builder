from .DirectiveBase import DirectiveBase
from Enums import OnOff

class MultiAcceptDirective(DirectiveBase):
    def __init__(
        self,
        on_off : OnOff = OnOff.on,
    ):
        super().__init__(
            "multi_accept",
            (on_off.name,),
        )
