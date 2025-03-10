from Directives.DirectiveBase import DirectiveBase

class DefaultTypeDirective(DirectiveBase):
    def __init__(
        self,
        mime_type : str = "application/octet-stream",
    ):
        super().__init__(
            "default_type",
            (mime_type,),
        )
