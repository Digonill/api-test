from src.core.rules.repeated_rule import RepeatedRule
from .abstract_rule import AbstractRule, ResultRule

class EmptyRule(AbstractRule):
    EMPTY_LETTER_FAILED = 'Whitespaces is not valid.'

    def apply(self, str_pwd: str) -> ResultRule:
        if str_pwd.count(' ') == 0:
            return self.next(str_pwd)
        else:
            return ResultRule(False, self.EMPTY_LETTER_FAILED)