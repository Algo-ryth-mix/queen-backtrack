import abc
from typing import List, Tuple


class RenderBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def render(self, positions: List[Tuple[int, int]]) -> None:
        pass
