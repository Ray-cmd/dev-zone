import string
import random

class Password:

    def __init__(self, length: int = 12, has_digits: bool = True, has_specials: bool = False) -> None:
        if not type(length) == int:
            raise ValueError("length must be an integer")
        if not type(has_digits) == bool:
            raise ValueError("has_digits must be an boolean")
        if not type(has_specials) == bool:
            raise ValueError("has_specials must be an boolean")

        self.__length = length
        self.__has_digits = has_digits
        self.__has_specials = has_specials
        self.__chars = self.__generate_array_of_chars()
        self.__value = self.__generate_password()

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, val: int) -> None:
        if not type(val) == int:
            raise ValueError("length must be an integer")
        if val != self.__length:
            self.__length = val
            self.__value = self.__generate_password()

    @property
    def has_digits(self):
        return self.__has_digits

    @has_digits.setter
    def has_digits(self, val: bool) -> None:
        if not type(val) == bool:
            raise ValueError("has_digits must be an boolean")
        if val != self.__has_digits:
            self.__has_digits = val
            self.__chars = self.__generate_array_of_chars()
            self.__value = self.__generate_password()

    @property
    def has_specials(self):
        return self.__has_specials

    @has_specials.setter
    def has_specials(self, val: bool) -> None:
        if not type(val) == bool:
            raise ValueError("has_specials must be an boolean")
        if val != self.__has_specials:
            self.__has_specials = val
            self.__chars = self.__generate_array_of_chars()
            self.__value = self.__generate_password()
        
    @property
    def value(self):
        return self.__value

    def __generate_array_of_chars(self) -> str:
        chars = string.ascii_lowercase + string.ascii_uppercase
        if self.__has_digits:
            chars += string.digits
        if self.__has_specials:
            chars += string.punctuation
        return chars

    def __generate_password(self) -> str:
        string = ""
        for i in range(0, self.__length):
            char = random.choice(self.__chars)
            string += char
        return string

    def __repr__(self) -> str:
        return self.__value

if __name__ == "__main__":
    print(Password(length=22, has_specials=True))