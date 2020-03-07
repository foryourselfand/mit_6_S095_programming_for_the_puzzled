from abc import ABC, abstractmethod
from typing import List

from structures import Interval


class PleaseConform(ABC):
    @abstractmethod
    def please_conform(self, caps: List[str]) -> List[Interval]:
        pass
