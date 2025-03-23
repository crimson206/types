# Converted from: packs.ipynb

from crimson.types.addon import TypesPack, T
from typing import List


class CustomType(TypesPack[T], List[int]):
    """
    my type with various type addons
    """

    validate_base_index = 1


CustomType[List[int], 1, 2]

CustomType.__metadata__

a = CustomType

a.append


def func(arg: CustomType[List[int]]):
    pass


from pydantic import BaseModel


class MyProps(BaseModel):
    my_arg: CustomType


props = MyProps(my_arg=[1, 2, 3])

props.my_arg
