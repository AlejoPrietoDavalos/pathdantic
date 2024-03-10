from typing import Type, TypeVar
from pathlib import Path

from pydantic import Field

from pathdantic.base import PathBase

__all__ = ["PathFolder"]

T_PathFolder = TypeVar("T_PathFolder", bound="PathFolder")

class PathFolder(PathBase):
    @classmethod
    def create(cls: Type[T_PathFolder], p: str | Path) -> T_PathFolder:
        p = Path(p)
        p.mkdir(exist_ok=True)

        fields_default = {}
        for field, field_type in cls.__annotations__.items():   # TODO: View subclasses fields.
            if field != "p":
                instance_field: T_PathFolder = field_type.create(p=p / field)
                fields_default[field] = instance_field.model_dump()
        _instance = cls(p=p, **fields_default)
        return _instance