import datetime

class Person():
    def __init__(self, last_name, first_name, birth_date, num_tel):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.num_tel = num_tel
        self.email = None
        self.address = None
      
    @property
    def last_name(self):
        return self.__last_name.capitalize()

    @last_name.setter
    def last_name(self, last_name):
        if not isinstance(last_name, str):
            raise TypeError("Last name must be a string")
        if len(last_name) < 2:
            raise ValueError("Last name must be at least 2 characters")
        if len(last_name) > 64:
            raise ValueError("Last name must not exceed 64 characters")
        self.__last_name = last_name.lower()
   
    @property
    def first_name(self):
        return self.__first_name.capitalize()

    @first_name.setter
    def first_name(self, first_name):
        if not isinstance(first_name, str):
            raise TypeError("First name must be a string")
        if len(first_name) < 2:
            raise ValueError("First name must be at lest 2 characters")
        if len(first_name) > 32:
            raise ValueError("First name must not exceed 32 characters")
        self.__first_name = first_name.lower()

    @property
    def birth_date(self):
        return datetime.datetime.fromtimestamp(self.__birth_date).strftime("%d.%m.%Y")

    @birth_date.setter
    def birth_date(self, birth_date):
        if not isinstance(birth_date, datetime.datetime) and not isinstance(birth_date, str):
            raise ValueError("Birth date must be a string or a datetime.datetime object")
        if isinstance(birth_date, str):
            birth_date = datetime.datetime.strptime(birth_date, "%d.%m.%Y")

        timestamp = birth_date.timestamp()
        self.__birth_date = timestamp

    @property
    def num_tel(self):
        return self.__num_tel

    @num_tel.setter
    def num_tel(self, num_tel):
        if not isinstance(num_tel, str):
            raise ValueError("Telephone number must be a string")
        num_tel = num_tel.replace(" ", "")
        if not num_tel.isdigit():
            raise ValueError("Telephone number must be made of numbers")
        if not len(num_tel) == 10:
            raise ValueError("Telephone number must be a 10 numbers swiss number") 

        self.__num_tel = num_tel

    def __str__(self):
        return f"Last name : {self.last_name} First name : {self.first_name} Birth date : {self.birth_date} Telephon : {self.num_tel}"

def main():
    #date = "23.08.1992"
    date = datetime.datetime.strptime("22.08.1992", "%d.%m.%Y")

    tel = "0244455902"

    tmp = Person("Ray", "Luca", date, tel)
    print(tmp)
    tmp.last_name = "Dylan"
    tmp.first_name = "Bob"
    tmp.birth_date = "01.01.1990"
    tmp.num_tel = "024 400 00 00"
    print(tmp)

main()