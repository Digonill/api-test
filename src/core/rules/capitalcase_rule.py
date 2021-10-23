from .abstract_rule import AbstractRule, ResultRule


class CapitalCaseRule(AbstractRule):
    CAPITAL_CASE_FAILED = "Required at least a capital letter."

    def apply(self, str_pwd: str) -> tuple:

        result = False

        # verify there are capitalcase
        for char in str_pwd:
            if char.isupper():
                result = True
                break

        return self.next(str_pwd) if result else ResultRule(False, self.CAPITAL_CASE_FAILED)
