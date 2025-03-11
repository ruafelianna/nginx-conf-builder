from Directives import (
    AccessLogDirective,
    DefaultTypeDirective,
    DirectiveBase,
    IncludeDirective,
    SendFileDirective,
)

class HttpContext(DirectiveBase):
    def __init__(
        self,
        includes : tuple[IncludeDirective] = (),
        default_type : DefaultTypeDirective = None,
        access_log : AccessLogDirective = None,
        sendfile : SendFileDirective = None,
    ):
        self.includes = includes
        self.default_type = default_type
        self.access_log = access_log
        self.sendfile = sendfile

        super().__init__(
            "http",
            block = self.includes
            + (
                self.default_type,
                self.access_log,
                self.sendfile,
            )
        )
