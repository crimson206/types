# Converted from: intelli_type.ipynb


from crimson.types.addon.intelli_type import IntelliHolder, T
from typing import Tuple


class CumstomType(Tuple[int, str], IntelliHolder[T]):
    """
    CustomType with complex structure init.\n
    We want to expose its inner structure by hover.\n
    Therefore, we let this type hold `IntelliHolder[T]`\n
    """


def intelli_holder_example(arg1: CumstomType[Tuple[int, str]]) -> None:
    pass
