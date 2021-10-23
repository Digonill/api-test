from src.core.validator_password import ValidatorPassword
import json
class MainController():
    def __init__(self) -> None:
        self.validate = ValidatorPassword()
        pass

    def isvalid(self, string_pwd: dict) -> object:

        if string_pwd is None:
            ValueError('Password invalid')

        result = self.validate.apply(string_pwd.get('text',''))

        if result.Status:
            return result, 201

        return result, 400


