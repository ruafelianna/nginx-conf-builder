from .DirectiveBase import DirectiveBase

class ServerNameDirective(DirectiveBase):
    def __init__(
        self,
        domains : tuple[str, ...] = ("",),
    ):
        if len(domains) < 1:
            ValueError("There should be at least one domain")

        super().__init__(
            "server_name",
            domains,
        )
