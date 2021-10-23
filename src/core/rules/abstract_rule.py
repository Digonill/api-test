from __future__ import annotations
from collections import namedtuple
from abc import abstractmethod
from .rule import Rule


ResultRule = namedtuple("ResultRule", "Status Mensagem")


class AbstractRule(Rule):
    _next_rule: Rule = None

    def appendNext(self, rule: Rule) -> Rule:
        self._next_rule = rule
        return rule

    def next(self, str_pwd: str) -> tuple:
        if self._next_rule is None:
            return ResultRule(True, 'Validate OK')

        return self._next_rule.apply(str_pwd)

    @abstractmethod
    def apply(self, str_pwd: str) -> tuple:
        if self._next_rule:
            return self._next_rule.apply(str_pwd)

    def is_validator(self) -> bool:
        return False
