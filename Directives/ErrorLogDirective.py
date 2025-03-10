from Enums.LogLevel import LogLevel
from Directives.DirectiveBase import DirectiveBase

class ErrorLogDirective(DirectiveBase):
    def __init__(
        self,
        file : str = "/var/log/nginx/error.log",
        log_level : LogLevel = LogLevel.notice,
    ):
        if not isinstance(log_level, LogLevel):
            raise TypeError("`log_level` must be a `LogLevel` enum member")

        super().__init__(
            "error_log",
            (file, log_level.name,),
        )
