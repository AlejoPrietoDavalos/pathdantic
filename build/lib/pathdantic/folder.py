from typing import Type, TypeVar
from pathlib import Path

from pydantic import Field

from pathdantic.base import PathBase

__all__ = ["PathFolder"]

T_PathFolder = TypeVar("T_PathFolder", bound="PathFolder")

class PathFolder(PathBase):
    name: str = Field(frozen=True)
    folder: Path = Field(frozen=True)

    @property
    def p(self) -> Path:
        return self.folder / self.name

    @classmethod
    def create(cls: Type[T_PathFolder], name: str, folder: Path) -> T_PathFolder:
        _path_folder = folder / name
        _path_folder.mkdir(exist_ok=True)

        fields_default = {}
        for field, field_type in cls.__annotations__.items():
            if field != "name" and field != "folder":
                instance_field: T_PathFolder = field_type.create(name=field, folder=_path_folder)
                fields_default[field] = instance_field.model_dump()
        _instance = cls(name=name, folder=folder, **fields_default)
        return _instance