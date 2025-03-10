from Directives.DirectiveBase import DirectiveBase
from Directives.AccessLogDirective import AccessLogDirective
from Directives.DefaultTypeDirective import DefaultTypeDirective
from Directives.IncludeDirective import IncludeDirective
from Directives.SendFileDirective import SendFileDirective

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
