from .DirectiveBase import DirectiveBase

class TryFilesDirective(DirectiveBase):
    def __init__(
        self,
        files : tuple[str, ...] = ("$uri",),
    ):
        if len(files) < 1:
            ValueError("There should be at least one file in the tuple")

        super().__init__(
            "try_files",
            files,
        )
