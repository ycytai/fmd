from typing import Any

from fmd.client import FmdApi


class ManagerBase:
    _obj: 'ObjectBase'

    def __init__(self, fa: FmdApi) -> None:
        self.fa = fa

    def get(self, **kwargs: Any) -> 'ObjectBase':
        return self._obj(self, **kwargs)


class ObjectBase:
    def __init__(self, manager: ManagerBase, **kwargs: Any) -> None:
        self.manger = manager
        self.__dict__.update(kwargs)
