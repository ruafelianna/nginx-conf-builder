from .DirectiveBase import DirectiveBase

class IncludeDirective(DirectiveBase):
    def __init__(
        self,
        mask : str = "/etc/nginx/mime.types",
    ):
        super().__init__(
            "include",
            (mask,),
        )
