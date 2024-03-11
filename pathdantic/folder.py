from typing import Type, TypeVar
from pathlib import Path

from pathdantic.base import BasePathStatic

__all__ = ["PathFolderStatic"]

T_PathFolderStatic = TypeVar("T_PathFolderStatic", bound="PathFolderStatic")

class PathFolderStatic(BasePathStatic):
    @classmethod
    def create(cls: Type[T_PathFolderStatic], p: Path) -> T_PathFolderStatic:
        _instance = cls.get_instance(p=p)
        _instance.mkdir(parents=True, exist_ok=True)
        return _instance

    def mkdir(self, mode: int = 511, parents: bool = True, exist_ok: bool = True) -> None:
        self.p.mkdir(mode=mode, parents=parents, exist_ok=exist_ok)
