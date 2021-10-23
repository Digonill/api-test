from .abstract_rule import AbstractRule, ResultRule


class SpecialCharRule(AbstractRule):
    SPECIAL_CHAR_FAILED = "Only special characters valid: !@#$%^&*()-+"
    SPECIAL_CHAR_EXP = '!@#$%^&*()-+'

    def apply(self, str_pwd: str) -> tuple:

        result = False

        for char in str_pwd:
            if char in self.SPECIAL_CHAR_EXP:
                result = True
                break


        return self.next(str_pwd) if result else ResultRule(result, self.SPECIAL_CHAR_FAILED) 
