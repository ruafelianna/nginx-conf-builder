from __future__ import annotations

from Common import *
from Contexts import *
from Directives import *
from Enums import *
from Generators import *

from SilvaViridis.Python.Common.Enums import OrderedEnum, OrderedEnumComparable

@OrderedEnumComparable(lambda cls: {
    A.a : 1,
    A.b : 0,
})
class A(OrderedEnum):
    a="dred"
    b="erdrd"

print(A.a <= A.b)
exit(0)
s1 = ServerContext(
    listens = (
        ListenDirective(
            unix_socket = "unix:/tmp/unix.sock",
            proxy_protocol = True,
            so_keepalive = Enum_OnOff.on,
        ),
    ),
)

s2 = ServerContext(
    listens = (
        ListenDirective(
            address = "localhost",
            default_server = True,
            accept_filter = ListenAcceptFilter.httpready,
            keepcnt = 30,
            bind = True,
            fastopen = 34,
        ),
        ListenDirective(
            unix_socket = "unix:/tmp/unix.sock",
            proxy_protocol = True,
            so_keepalive = Enum_OnOff.on,
        ),
    ),
    server_name = ServerNameDirective(("example.com", "*.example.com")),
    index = IndexDirective(("index.html", "index.php")),
    root = RootDirective(),
    locations = (
        LocationContext(
            template = "/images/hello.png",
            modifier = LocationModifier.exact_match,
            proxy_pass = ProxyPassDirective("http://localhost:8080"),
        ),
        LocationContext(
            template = "/images/",
            modifier = LocationModifier.regex_match_case_insensitive,
            proxy_pass = ProxyPassDirective("http://localhost:8081"),
            try_files = TryFilesDirective(),
        ),
    ),
)

d = MainContext(
    user = UserDirective(),
    worker_processes = WorkerProcessesDirective(),
    error_log = ErrorLogDirective(),
    pid = PidDirective(),
    event_ctx = EventContext(
        worker_connections = WorkerConnectionsDirective(),
        use = UseDirective(EventHandleMethod.dev_poll),
        multi_accept = MultiAcceptDirective(),
    ),
    http_ctx = HttpContext(
        includes = (
            IncludeDirective(),
            IncludeDirective("/etc/nginx/conf.d/*.conf"),
        ),
        default_type = DefaultTypeDirective(),
        access_log = AccessLogDirective(),
        sendfile = SendFileDirective(),
        servers = (
            s2,
            s1,
        ),
    ),
)

gen = CrossplaneGenerator()

print(gen.build_many((s1, s2)))

print(gen.build(d))
