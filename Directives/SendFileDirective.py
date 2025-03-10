from Directives.DirectiveBase import DirectiveBase
from Enums.OnOff import OnOff

class SendFileDirective(DirectiveBase):
    def __init__(
        self,
        on_off : OnOff = OnOff.on,
    ):
        if not isinstance(on_off, OnOff):
            raise TypeError("`on_off` must be a `OnOff` enum member")

        super().__init__(
            "sendfile",
            (on_off.name,),
        )
