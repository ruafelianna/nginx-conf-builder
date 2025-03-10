from Directives.DirectiveBase import DirectiveBase

class WorkerProcessesDirective(DirectiveBase):
    def __init__(
        self,
        count : int | None = None,
    ):
        super().__init__(
            "worker_processes",
            ("auto",) if count is None else (str(count),),
        )
