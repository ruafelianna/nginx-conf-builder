from Common import DirectiveBase
from Enums import EventHandleMethod

class UseDirective(DirectiveBase):
    def __init__(
        self,
        method : EventHandleMethod = EventHandleMethod.select,
    ):
        super().__init__(
            "use",
            (method.name,),
        )
