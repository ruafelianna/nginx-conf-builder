from Directives import (
    DirectiveBase,
    IndexDirective,
    ListenDirective,
    RootDirective,
    ServerNameDirective,
)

class ServerContext(DirectiveBase):
    def __init__(
        self,
        listens : tuple[ListenDirective] = (),
        index : IndexDirective | None = None,
        root : RootDirective | None = None,
        server_name : ServerNameDirective | None = None,
    ):
        self.listens = listens
        self.index = index
        self.root = root
        self.server_name = server_name

        super().__init__(
            "server",
            block = self.listens
            + (
                self.server_name,
                self.root,
                self.index,
            )
        )
