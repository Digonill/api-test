from unittest import TestCase
from src.controller import MainController
from src.core.rules import RepeatedRule

class test_main_controller(TestCase):

    #call before test
    def setUp(self) -> None:
        self.instance = MainController()
    
    def test_controller_success(self):

        result = self.instance.isvalid(
            {
                "text": "test"
            })
        
        self.assertNotIsInstance(result, RepeatedRule)
        
    
    def test_controller_error(self):
        with self.assertRaises(ValueError):
            self.instance.isvalid(None)
