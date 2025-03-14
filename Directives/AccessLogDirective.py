from Common import DirectiveBase

class AccessLogDirective(DirectiveBase):
    def __init__(
        self,
        file : str | None = "/var/log/nginx/access.log",
        format : str | None = None,
    ):
        super().__init__(
            "access_log",
            ("off",) if file is None else \
                (file,) if format is None else \
                    (file, format,),
        )
