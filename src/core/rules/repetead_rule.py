from abstract_rule import AbstractRule

class RepeatedRule(AbstractRule):
    REPEATED_CHAR = "Don't allow repeated letters."

    def apply(self, str_pwd: str) -> tuple:

        result = True

        for char in str_pwd:
            # checking if there duplicate
            if str_pwd.count(char) > 1:
                result = False
        
        return super()._next_rule(str_pwd) if result  else False, self.REPEATED_CHAR
        

        