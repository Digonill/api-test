from unittest import TestCase
from src.core.rules import (
    CapitalCaseRule,
    LowerCaseRule,
    EmptyRule,
    RepeatedRule,
    SpecialCharRule,
    LengthRule
)


class test_rule(TestCase):

    def test_capitalcase_sucess(self):

        rule = CapitalCaseRule()

        result = rule.apply(str_pwd='Senha')

        self.assertTrue(result.Status, result.Mensagem)

    def test_capitalcase_error(self):
        rule = CapitalCaseRule()

        result = rule.apply(str_pwd='senha')

        self.assertFalse(result.Status, result.Mensagem)

    def test_empty_sucess(self):
        rule = EmptyRule()

        result = rule.apply('NXOXOX')

        self.assertTrue(result.Status, result.Mensagem)

    def test_empty_error(self):
        rule = EmptyRule()

        result = rule.apply('NX OXOX')

        self.assertFalse(result.Status, result.Mensagem)

    def test_repeated_sucess(self):
        rule = RepeatedRule()

        result = rule.apply('x12345z')

        self.assertTrue(result.Status, result.Mensagem)

    def test_repeated_error(self):
        rule = RepeatedRule()

        result = rule.apply('x123345z')

        self.assertFalse(result.Status, result.Mensagem)

    def test_lowercase_sucess(self):
        rule = LowerCaseRule()

        result = rule.apply('xAAAAvbz')

        self.assertTrue(result.Status, result.Mensagem)

    def test_lowercase_error(self):
        rule = LowerCaseRule()

        result = rule.apply('SSSREWEF')

        self.assertFalse(result.Status, result.Mensagem)

    def test_specialchar_sucess(self):
        rule = SpecialCharRule()

        result = rule.apply('@lskaAAvbz')

        self.assertTrue(result.Status, result.Mensagem)
    
    def test_specialchar_error_invalid(self):
        rule = SpecialCharRule()

        result = rule.apply('lsb$aB#?X')

        self.assertFalse(result.Status, result.Mensagem)

    def test_specialchar_error(self):
        rule = SpecialCharRule()

        result = rule.apply('SSSREWEF')

        self.assertFalse(result.Status, result.Mensagem)

    def test_length_success(self):
        rule = LengthRule()

        result = rule.apply('SSSREWEF99')

        self.assertTrue(result.Status, result.Mensagem)

    def test_specialchar_error(self):
        rule = LengthRule()

        result = rule.apply('ss')

        self.assertFalse(result.Status, result.Mensagem)
