from .abstract_rule import AbstractRule, ResultRule


class LowerCaseRule(AbstractRule):
    LOWERCASE_FAILED = "Required at least a lowercase letter."

    def apply(self, str_pwd: str) -> ResultRule:

        result = False

        for char in str_pwd:
            if char.islower():
                result = True
                break

        return self.next(str_pwd) if result else ResultRule(False, self.LOWERCASE_FAILED)
