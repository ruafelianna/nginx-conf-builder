from Contexts.EventContext import EventContext
from Directives.ErrorLogDirective import ErrorLogDirective
from Directives.DirectiveBase import DirectiveBase
from Directives.PidDirective import PidDirective
from Directives.UserDirective import UserDirective
from Directives.WorkerProcessesDirective import WorkerProcessesDirective

class MainContext(DirectiveBase):
    def __init__(
        self,
        user : UserDirective = None,
        worker_processes : WorkerProcessesDirective = None,
        error_log : ErrorLogDirective = None,
        pid : PidDirective = None,
        event_ctx : EventContext = None,
    ):
        self.user = user
        self.worker_processes = worker_processes
        self.error_log = error_log
        self.pid = pid
        self.event_ctx = event_ctx

        super().__init__(
            "main",
            block = (
                self.user,
                self.worker_processes,
                self.error_log,
                self.pid,
                self.event_ctx,
            )
        )
