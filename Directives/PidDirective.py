from .DirectiveBase import DirectiveBase

class PidDirective(DirectiveBase):
    def __init__(
        self,
        file : str = "/run/nginx.pid",
    ):
        super().__init__(
            "pid",
            (file,),
        )
