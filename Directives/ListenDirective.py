from .DirectiveBase import DirectiveBase
from Enums import ListenAcceptFilter, OnOff
from Utils import BuildArgsHelper

class ListenDirective(DirectiveBase):
    def __init__(
        self,
        address : str | None = None,
        port : int | None = None,
        unix_socket : str | None = None,
        default_server : bool = False,
        ssl : bool = False,
        quic : bool = False,
        proxy_protocol : bool = False,
        setfib : int | None = None,
        fastopen : int | None = None,
        backlog : int | None = None,
        rcvbuf : int | None = None,
        sndbuf : int | None = None,
        accept_filter : ListenAcceptFilter | None = None,
        deferred : bool = False,
        bind : bool = False,
        ipv6only : OnOff | None = None,
        reuseport : bool = False,
        so_keepalive : OnOff | None = None,
        keepidle : str | None = None,
        keepintvl : str | None = None,
        keepcnt : int | None = None,
    ):
        if unix_socket and (address or port):
            raise ValueError("`unix_socket` cannot be combined with `address` or `port`")

        if not any((unix_socket, address, port)):
            raise ValueError("One of the values should be set: `address`, `port`, `unix_socket`")

        if unix_socket and not unix_socket.startswith("unix:"):
            raise ValueError("`unix_socket` should start with `unix:`")

        if unix_socket and (setfib or fastopen or ipv6only or reuseport):
            raise ValueError("`unix_socket` cannot be combined with `setfib`, `fastopen`, `ipv6only` or `reuseport`")

        if so_keepalive and (keepidle or keepintvl or keepcnt):
            raise ValueError("`so_keepalive` on/off value cannot be combined with `keepidle`, `keepintvl` or `keepcnt`")

        args = []

        if unix_socket:
            BuildArgsHelper.add_str(args, unix_socket)
        elif not address:
            BuildArgsHelper.add_str(args, str(port))
        elif not port:
            BuildArgsHelper.add_str(args, address)
        else:
            BuildArgsHelper.add_str(args, f"{address}:{port}")

        BuildArgsHelper.add_bool(args, "default_server", default_server)
        BuildArgsHelper.add_bool(args, "ssl", ssl)
        BuildArgsHelper.add_bool(args, "quic", quic)
        BuildArgsHelper.add_bool(args, "proxy_protocol", proxy_protocol)
        BuildArgsHelper.add_value(args, "setfib", setfib)
        BuildArgsHelper.add_value(args, "fastopen", fastopen)
        BuildArgsHelper.add_value(args, "backlog", backlog)
        BuildArgsHelper.add_value(args, "rcvbuf", rcvbuf)
        BuildArgsHelper.add_value(args, "sndbuf", sndbuf)
        BuildArgsHelper.add_enum(args, "accept_filter", accept_filter)
        BuildArgsHelper.add_bool(args, "deferred", deferred)
        BuildArgsHelper.add_bool(args, "bind", bind)
        BuildArgsHelper.add_enum(args, "ipv6only", ipv6only)
        BuildArgsHelper.add_bool(args, "reuseport", reuseport)
        BuildArgsHelper.add_enum(args, "so_keepalive", so_keepalive)

        if keepidle is not None or keepintvl is not None or keepcnt is not None:
            BuildArgsHelper.add_value(args, "so_keepalive", ListenDirective._create_keepalive(keepidle, keepintvl, keepcnt))

        super().__init__(
            "listen",
            tuple(args),
        )

    @staticmethod
    def _create_keepalive(
        keepidle : str | None = None,
        keepintvl : str | None = None,
        keepcnt : int | None = None,
    ) -> str:
        keepidle = BuildArgsHelper.value_or_empty(keepidle)
        keepintvl = BuildArgsHelper.value_or_empty(keepintvl)
        keepcnt = BuildArgsHelper.value_or_empty(keepcnt)
        return f"{keepidle}:{keepintvl}:{keepcnt}"
