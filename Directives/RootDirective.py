from .DirectiveBase import DirectiveBase

class RootDirective(DirectiveBase):
    def __init__(
        self,
        path : str = "/var/www/html",
    ):
        super().__init__(
            "root",
            (path,),
        )
