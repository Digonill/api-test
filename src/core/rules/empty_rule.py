from .abstract_rule import AbstractRule, ResultRule

class EmptyRule(AbstractRule):
    EMPTY_LETTER_FAILED = 'Whitespaces is not valid.'

    def apply(self, str_pwd: str) -> tuple:
        if str_pwd.count(' ') == 0:
            return self.next(str_pwd) #_next_rule.apply(str_pwd) 
        else:
            return ResultRule(False, self.EMPTY_LETTER_FAILED)