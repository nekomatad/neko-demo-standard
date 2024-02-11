from abc import ABC, abstractmethod


class DemoInterface(ABC):
    """
    Includes only static methods that would be regular functions outside of classes if
    you were developing a regular python module
    """
    @staticmethod
    @abstractmethod
    def some_very_useful_method(very_important_arg: str = "h") -> None:
        """
        Include docstrings here, in standards
        :param very_important_arg: Probably this one is important
        :return:
        """


__all__ = [DemoInterface]
__replacements__ = __all__
