from Directives.DirectiveBase import DirectiveBase
from Directives.MultiAcceptDirective import MultiAcceptDirective
from Directives.UseDirective import UseDirective
from Directives.WorkerConnectionsDirective import WorkerConnectionsDirective

class EventContext(DirectiveBase):
    def __init__(
        self,
        worker_connections : WorkerConnectionsDirective = None,
        use : UseDirective = None,
        multi_accept : MultiAcceptDirective = None,
    ):
        self.worker_connections = worker_connections
        self.use = use
        self.multi_accept = multi_accept

        super().__init__(
            "events",
            block = (
                self.worker_connections,
                self.use,
                self.multi_accept,
            )
        )
