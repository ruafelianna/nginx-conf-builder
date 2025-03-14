from Common import DirectiveBase

class ProxyPassDirective(DirectiveBase):
    def __init__(
        self,
        url : str,
    ):
        super().__init__(
            "proxy_pass",
            (url,),
        )
