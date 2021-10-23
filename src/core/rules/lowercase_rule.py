from .abstract_rule import AbstractRule, ResultRule


class LowerCaseRule(AbstractRule):
    LOWERCASE_FAILED = "Required at least a lowercase letter."

    def apply(self, str_pwd: str) -> tuple:

        result = False

        for char in str_pwd:
            if char.islower():
                result = True
                break

        return self._next_rule.apply(str_pwd) if result else ResultRule(False, self.LOWERCASE_FAILED)
