import string
import random

class PwdGen:
    __LOWERCASES = string.ascii_lowercase
    __UPPERCASES = string.ascii_uppercase
    __NUMBERS = string.digits
    __SYMBOLS = string.punctuation

    __nbr_char = 12
    __lowercase = True
    __uppercase = True
    __number = True
    __symbol = False
    __password = ""

    def __init__(self, nbr_char = None, lowercase = None, uppercase = None, number = None, symbol = None):
        if nbr_char is not None:
            self.__nbr_char = nbr_char
        if lowercase is not None:
            self.__lowercase = lowercase
        if uppercase is not None:
            self.__uppercase = uppercase
        if number is not None:
            self.__number = number
        if symbol is not None:
            self.__symbol = symbol
        self.generate()


    @property
    def nbr_char(self):
        return self.__nbr_char

    @nbr_char.setter
    def nbr_char(self, nbr_char):
        if not isinstance(nbr_char, int):
            raise TypeError("nbr_char must be an integer")
        if nbr_char < 6 and nbr_char > 128:
            raise ValueError("nbr_char must be between 6 and 128 characters")
        self.__nbr_char = nbr_char

    @property
    def lowercase(self):
        return self.__lowercase

    @lowercase.setter
    def lowercase(self, lowercase):
        if not isinstance(lowercase, bool):
            raise TypeError("lowercase must be a booleen")
        self.__lowercase = lowercase

    @property
    def uppercase(self):
        return self.__uppercase

    @uppercase.setter
    def uppercase(self, uppercase):
        if not isinstance(uppercase, bool):
            raise TypeError("uppercase must be a booleen")
        self.__uppercase = uppercase

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if not isinstance(number, bool):
            raise TypeError("number must be a booleen")
        self.__number = number

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol):
        if not isinstance(symbol, bool):
            raise TypeError("symbol must be a booleen")
        self.__symbol = symbol
        
    def __make_sample(self):
        sample = ""
        if self.lowercase:
            sample += self.__LOWERCASES
        if self.uppercase:
            sample += self.__UPPERCASES
        if self.number:
            sample += self.__NUMBERS
        if self.symbol:
            sample += self.__SYMBOLS
        return sample

    def generate(self):
        sample = self.__make_sample()
        password = ""
        for _ in range(self.nbr_char):
            password += random.choice(sample)
        self.__password = password
        
    def __str__(self):
        return str(self.__password)

    def __repr__(self):
        return str(self.__password)

def main():
    PwdGen.symbol = True
    for _ in range(5):
        print(PwdGen())

if __name__ == '__main__':
    main()