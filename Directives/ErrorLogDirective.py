from .DirectiveBase import DirectiveBase
from Enums import LogLevel

class ErrorLogDirective(DirectiveBase):
    def __init__(
        self,
        file : str = "/var/log/nginx/error.log",
        log_level : LogLevel = LogLevel.notice,
    ):
        super().__init__(
            "error_log",
            (file, log_level.name,),
        )
