from typing import Type, TypeVar
from pathlib import Path

from pydantic import Field

from pathdantic.base import BasePath

__all__ = ["PathRoot"]

T_PathRoot = TypeVar("T_PathRoot", bound="PathRoot")

class PathRoot(BasePath):
    name: str = Field(frozen=True)

    @property
    def p(self) -> Path:
        return Path(self.name)

    @classmethod
    def how_to_instantiate(cls: Type[T_PathRoot], name: str) -> T_PathRoot:
        assert isinstance(name, str), "Debe ser instancia de string."
        _path_root = Path(name)
        _path_root.mkdir(exist_ok=True)

        fields_default = {}
        for field, field_type in cls.__annotations__.items():
            if field != "name":
                instance_field = field_type.create(name=field, folder=_path_root)
                fields_default[field] = instance_field.model_dump()
        instance_root = cls(name=name, **fields_default)
        instance_root.mkdir()
        return instance_root