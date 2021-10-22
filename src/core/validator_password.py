from typing import List

from src.core.rules import capitalcase_rule
from core.rules.abstract_rule import AbstractRule
from core.rules.capitalcase_rule import CapitalCaseRule
from core.rules.empty_rule import EmptyRule
from core.rules.lowercase_rule import LowerCaseRule
from core.rules.repetead_rule import RepeatedRule
from core.rules.specialchar_rule import SpecialCharRule


class ValidatorPassword():

    def __init__(self) -> None:
        self.__rule = AbstractRule()

        self.__rule.appendNext(
            CapitalCaseRule()).appendNext(
            EmptyRule()).appendNext(
            LowerCaseRule()).appendNext(
            RepeatedRule()).appendNext(
            SpecialCharRule())

    def apply(self, str_pwd: str) -> tuple:
        return self.__rule.apply(str_pwd)
