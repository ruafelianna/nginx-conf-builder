from Common import DirectiveBase

class WorkerConnectionsDirective(DirectiveBase):
    def __init__(
        self,
        count : int = 1024,
    ):
        super().__init__(
            "worker_connections",
            (str(count),),
        )
