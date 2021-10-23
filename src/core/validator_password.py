from .rules import CapitalCaseRule, EmptyRule, LowerCaseRule, RepeatedRule, SpecialCharRule


class ValidatorPassword():

    def __init__(self) -> None:
        self.__rule = EmptyRule()

        self.__rule.appendNext(
            CapitalCaseRule()).appendNext(
            LowerCaseRule()).appendNext(
            RepeatedRule()).appendNext(
            SpecialCharRule())

    def apply(self, str_pwd: str) -> tuple:
        return self.__rule.apply(str_pwd)
