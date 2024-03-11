from typing import Type, TypeVar, Generator, Tuple, Dict
from abc import ABC, abstractclassmethod
from pathlib import Path

from pydantic import BaseModel, Field

__all__ = ["BasePath", "BasePathStatic", "BasePathDinamic"]

_SPECIAL_FIELDS = ["p"]     # TODO: Can't use this names for own classes. Make restrictions.

T_BasePath = TypeVar("T_BasePath", bound="BasePath")

class BasePath(BaseModel, ABC):
    p: Path = Field(frozen=True)

    @classmethod
    def iter_fields(cls: Type[T_BasePath]) -> Generator[Tuple[str, Type[T_BasePath]], None, None]:
        for field, field_info in cls.model_fields.items():
            if field not in _SPECIAL_FIELDS:
                field_annotation: Type[T_BasePath] = field_info.annotation
                yield field, field_annotation

    @classmethod
    def get_extra_fields(cls: Type[T_BasePath], p: Path) -> Dict[str, T_BasePath]:
        fields_default = {}
        for field, field_annotation in cls.iter_fields():
            _instance = field_annotation.create(p=p / field)
            fields_default[field] = _instance.model_dump()
        return fields_default

    @classmethod
    def get_instance(cls: Type[T_BasePath], p: Path) -> T_BasePath:
        _instance = cls(p=p, **cls.get_extra_fields(p=p))
        return _instance

    @abstractclassmethod
    def create(cls: Type[T_BasePath], p: Path) -> T_BasePath:
        ...


T_BasePathStatic = TypeVar("T_BasePathStatic", bound="BasePathStatic")

class BasePathStatic(BasePath):
    pass


T_BasePathDinamic = TypeVar("T_BasePathDinamic", bound="BasePathDinamic")

class BasePathDinamic(BasePath):
    pass

