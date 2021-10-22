from .abstract_rule import AbstractRule

class EmptyRule(AbstractRule):
    EMPTY_LETTER_FAILED = 'Whitespaces is not valid.'

    def apply(self, str_pwd: str) -> tuple:
        return super()._next_rule(str_pwd) if str_pwd.count(' ') == 0  else False, self.EMPTY_LETTER_FAILED