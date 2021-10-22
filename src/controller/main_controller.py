from core.validator_password import ValidatorPassword


class MainController():
    def __init__(self) -> None:
        self.validate = ValidatorPassword()
        pass

    def isvalid(self, string_pwd: str) -> bool:
        return self.validate.apply(string_pwd)
