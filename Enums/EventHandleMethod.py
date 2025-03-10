from enum import Enum
from types import DynamicClassAttribute

class EventHandleMethod(Enum):
    select = 0 # Standard
    poll = 1 # Standard
    kqueue = 2 # Unix
    epoll = 3 # Linux
    dev_poll = 4 # Solaris
    eventport = 5 # Solaris

    @DynamicClassAttribute
    def name(self):
        name = super(EventHandleMethod, self).name
        return "/dev/poll" if name == "dev_poll" else name
