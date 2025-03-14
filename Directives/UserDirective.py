from Common import DirectiveBase

class UserDirective(DirectiveBase):
    def __init__(
        self,
        user : str = "nginx",
        group : str | None = None,
    ):
        super().__init__(
            "user",
            (user,) if group is None else (user, group,),
        )
