from Common import DirectiveBase

class IndexDirective(DirectiveBase):
    def __init__(
        self,
        files : tuple[str, ...] = ("index.html",),
    ):
        if len(files) < 1:
            ValueError("There should be at least one index file")

        super().__init__(
            "index",
            files,
        )
