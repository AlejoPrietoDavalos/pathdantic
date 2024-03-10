from pathlib import Path

from pydantic import BaseModel, Field

class PathBase(BaseModel):
    p: Path = Field(frozen=True)

    def mkdir(self, mode: int = 511, parents: bool = False, exist_ok: bool = True) -> None:
        self.p.mkdir(mode=mode, parents=parents, exist_ok=exist_ok)

    # def __str__(self) -> str:
    #     return repr(self)

    # def __repr__(self) -> str:
    #     return repr(self.p)