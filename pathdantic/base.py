from pydantic import BaseModel

class PathBase(BaseModel):
    def mkdir(self, mode: int = 511, parents: bool = False, exist_ok: bool = True) -> None:
        self.p.mkdir(mode=mode, parents=parents, exist_ok=exist_ok)

    # def __str__(self) -> str:
    #     return repr(self)

    # def __repr__(self) -> str:
    #     return repr(self.p)