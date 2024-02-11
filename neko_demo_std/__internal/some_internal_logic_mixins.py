from abc import ABC, abstractmethod


class FirstAbstractMixin(ABC):
    """
    You can force implementation developer to use mixins for logic
    """
    @abstractmethod
    def first_method(self) -> None:
        ...


class SecondAbstractMixin(ABC):
    @abstractmethod
    def second_method(self) -> None:
        ...


"""
Or just leave one abstractclass, that can be split into mixins by implementation
developer
"""
