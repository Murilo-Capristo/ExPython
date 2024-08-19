from typing import Literal
from numpy import _SupportsWrite
import calculos
def arrasar(
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
    file: _SupportsWrite[str] | None = None,
    flush: Literal[False] = False
): None

arrasar("Programa para somar")


