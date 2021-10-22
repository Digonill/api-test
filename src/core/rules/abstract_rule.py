from __future__ import annotations
from abc import abstractmethod
from rules import Rule

class AbstractRule(Rule):
    _next_rule: Rule = None

    def appendNext(self, rule: Rule) -> Rule:
        self._next_rule = rule
        return rule

    @abstractmethod
    def apply(self, str_pwd: str) -> tuple:
        if self._next_rule:
            return self._next_rule.apply(str_pwd)
    

    def is_validator(self) -> bool:
        return False