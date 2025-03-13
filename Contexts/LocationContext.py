from Directives import (
    DirectiveBase,
    ProxyPassDirective,
    TryFilesDirective,
)

from Enums import LocationModifier
from Utils import BuildArgsHelper

class LocationContext(DirectiveBase):
    def __init__(
        self,
        template : str = "/",
        modifier : LocationModifier | None = None,
        proxy_pass : ProxyPassDirective | None = None,
        try_files : TryFilesDirective | None = None,
    ):
        self.template = template
        self.modifier = modifier
        self.proxy_pass = proxy_pass
        self.try_files = try_files

        args = []

        BuildArgsHelper.add_str(args, modifier.value)
        BuildArgsHelper.add_str(args, template)

        super().__init__(
            "location",
            tuple(args),
            block = (
                self.proxy_pass,
                self.try_files,
            )
        )
