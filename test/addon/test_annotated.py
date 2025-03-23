# Converted from: annotated.ipynb

from crimson.types.addon.annotated import AnnotatedType, annotated_type


class CommonClass(str):
    pass


# NBVAL_SKIP

try:
    CommonClass["Any Meta Data", [1, 3, 4]]
except Exception as e:
    print(e)


class CustomType(AnnotatedType, str):
    """
    Enhances str with built-in metadata annotation support.

    By inheriting from AnnotatedType, this class directly implements
    metadata annotation functionality. Use square brackets to provide
    additional information, e.g., CustomType2[max_length, encoding].

    This approach offers more control over annotation behavior
    compared to the @annotate decorator method.
    """


def func(arg: CustomType["Any Meta Data", [1, 3, 4]]):
    arg.split
    pass


CustomType.__metadata__


@annotated_type
class CustomType(str):
    """
    Annotatible Custom Type
    """


CustomType[1, 2, 3]

CustomType.__metadata__
