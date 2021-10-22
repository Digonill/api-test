from __future__ import annotations
from abc import ABC, abstractmethod


class Rule(ABC):

    @abstractmethod
    def appendNext(self, rule: Rule) -> Rule:
        pass

    @abstractmethod
    def apply(self, str_pwd: str) -> tuple:
        pass