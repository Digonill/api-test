from .abstract_rule import AbstractRule


class SpecialCharRule(AbstractRule):
    SPECIAL_CHAR_FAILED = "Only special characters valid: !@#$%^&*()-+"
    SPECIAL_CHAR_EXP = '!@#$%^&*()-+'

    def apply(self, str_pwd: str) -> tuple:
        if any(c in self.SPECIAL_CHAR_EXP for c in str_pwd):
            return self._next_rule.apply(str_pwd)
        
        return False, self.SPECIAL_CHAR_FAILED
