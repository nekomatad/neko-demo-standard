from ..__internal.some_internal_logic_mixins import (
    FirstAbstractMixin,
    SecondAbstractMixin,
)
from abc import ABC, abstractmethod


class SomeDemoClass(
    FirstAbstractMixin,
    SecondAbstractMixin,
    ABC
):
    """
    ABC needs to be LAST thing here
    """
    pass


class SomeOtherDemoClass(ABC):
    @abstractmethod
    def first_method(self) -> None:
        ...

    @abstractmethod
    def second_method(self) -> None:
        ...


__all__ = [SomeDemoClass, SomeOtherDemoClass]
__replacements__ = __all__

"""
Everything that is indicated in the list of replacements must be created directly in 
same file to simplify the structure, otherwise the implementation developer will 
have to completely repeat the structure of the internal folders with mixins that were 
created in the standard.
Mixins can be imported from internals of standard
"""
