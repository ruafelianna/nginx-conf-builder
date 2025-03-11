from .DirectiveBase import DirectiveBase
from Enums import EventHandleMethod

class UseDirective(DirectiveBase):
    def __init__(
        self,
        method : EventHandleMethod = EventHandleMethod.select,
    ):
        if not isinstance(method, EventHandleMethod):
            raise TypeError("`method` must be a `EventHandleMethod` enum member")

        super().__init__(
            "use",
            (method.name,),
        )
