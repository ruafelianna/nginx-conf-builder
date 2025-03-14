from Common import DirectiveBase, Enum_OnOff

class SendFileDirective(DirectiveBase):
    def __init__(
        self,
        on_off : Enum_OnOff = Enum_OnOff.on,
    ):
        super().__init__(
            "sendfile",
            (on_off.name,),
        )
