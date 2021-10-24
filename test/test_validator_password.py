from unittest import TestCase
from src.core import ValidatorPassword
from src.core.rules import ResultRule


class test_validator_password(TestCase):

    def setUp(self) -> None:
        self.instance = ValidatorPassword()

    def test_validator_sucess(self):

        result = self.instance.apply('adfadsfadsf')

        self.assertIsInstance(result, ResultRule)
