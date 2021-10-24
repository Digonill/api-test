from .abstract_rule import AbstractRule, ResultRule


class LengthRule(AbstractRule):

    MIN_LEN_FAILED = "Required minimum is nine char"

    def apply(self, str_pwd: str) -> ResultRule:

        return self.next(str_pwd) if len(str_pwd) >= 9 and len(str_pwd) <= 20 else ResultRule(False, self.MIN_LEN_FAILED)
