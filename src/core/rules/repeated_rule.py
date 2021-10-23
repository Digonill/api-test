from .abstract_rule import AbstractRule, ResultRule


class RepeatedRule(AbstractRule):
    REPEATED_CHAR = "Don't allow repeated letters."

    def apply(self, str_pwd: str) -> tuple:

        result = True

        for char in str_pwd:
            # checking if there duplicate
            if str_pwd.count(char) > 1:
                result = False
                break

        return self.next(str_pwd) if result else ResultRule(False, self.REPEATED_CHAR)
