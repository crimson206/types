# Converted from: number.ipynb

from crimson.types.control.number import IntRange, FloatRange


def case1(dropout: FloatRange[float, 0, 1]):
    """
    Looks Prettier
    """
    # arg was annotated properly
    dropout.imag
    pass


def case2(dropout: FloatRange[float, r"(0,1]]"]):
    """
    Strict information can be given
    """
    dropout.imag
    pass


def case3(depth: IntRange[int, 3, 12]):
    """
    We need different Custom types for different base types.

    See Below.
    """
    depth.real
    pass


from typing import TypeVar, Generic, Union

Num = TypeVar("Num", bound=Union[int, float])


class AnyRange(Generic[Num]):
    pass


def case4(dropout: AnyRange[float]):
    # AnyRange[float] is not `float`.
    # I won't explain why. For more details, study the `Generic type`.
    dropout.imag
