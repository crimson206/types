# Converted from: pydantic_compatible.ipynb

from typing import List
from pydantic import BaseModel, ConfigDict
from crimson.types.addon.pydantic import PydanticCompatible


class MyType(List[int]):
    """
    My Custom
    """


class MyProps(BaseModel):
    my_arg: MyType

    model_config = ConfigDict(arbitrary_types_allowed=True)


try:
    MyProps(my_arg=[1, 2, 3])
except Exception as e:
    print(e)


class MyCompatibleType(List[int], PydanticCompatible):
    """
    My Custom
    """


class MyProps(BaseModel):
    my_arg: MyCompatibleType


MyProps(my_arg=[1, 2, 3])


class MyCompatibleType(PydanticCompatible, List[int]):
    """
    My Custom
    """

    validate_base_index = 1


class MyProps(BaseModel):
    my_arg: MyCompatibleType


MyProps(my_arg=[1, 2, 3])


class MyCompatibleType(PydanticCompatible, List[int]):
    """
    My Custom
    """


class MyProps(BaseModel):
    my_arg: MyCompatibleType


try:
    MyProps(my_arg=[1, 2, 3])
except Exception as e:
    print(e)
