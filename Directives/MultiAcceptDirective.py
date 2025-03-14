from Common import DirectiveBase, Enum_OnOff

class MultiAcceptDirective(DirectiveBase):
    def __init__(
        self,
        on_off : Enum_OnOff = Enum_OnOff.on,
    ):
        super().__init__(
            "multi_accept",
            (on_off.name,),
        )
