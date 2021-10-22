from .abstract_rule import AbstractRule


class LowerCaseRule(AbstractRule):
    LOWERCASE_FAILED = "Required at least a lowercase letter."

    def apply(self, str_pwd: str) -> tuple:

        result = False

        for char in str_pwd:
            if char.islower():
                result = True
                break

        return super()._next_rule(str_pwd) if result else False, self.LOWERCASE_FAILED
