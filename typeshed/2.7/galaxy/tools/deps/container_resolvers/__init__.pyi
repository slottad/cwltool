# Stubs for galaxy.tools.deps.container_resolvers (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from galaxy.util.dictifiable import Dictifiable

class ContainerResolver(Dictifiable):
    dict_collection_visible_keys = ...  # type: Any
    __metaclass__ = ...  # type: Any
    app_info = ...  # type: Any
    resolver_kwds = ...  # type: Any
    def __init__(self, app_info: Optional[Any] = ..., **kwds) -> None: ...
    def resolve(self, tool_info): ...
    def resolver_type(self): ...