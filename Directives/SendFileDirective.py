from .DirectiveBase import DirectiveBase
from Enums import OnOff

class SendFileDirective(DirectiveBase):
    def __init__(
        self,
        on_off : OnOff = OnOff.on,
    ):
        super().__init__(
            "sendfile",
            (on_off.name,),
        )
