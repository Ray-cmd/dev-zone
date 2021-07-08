from address import Address

import datetime
import re

class Person():
    def __init__(self, last_name, first_name, birth_date, num_tel, email = None, address_infos = None):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.num_tel = num_tel
        self.email = email
        self.address_infos = address_infos
      
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

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        if email is None:
            self.__email = email
            return
        if not isinstance(email, str):
            raise ValueError("Email must be a string")
        if not re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email):
            raise ValueError("Email is not valid")
        self.__email = email
    

    @property
    def address_infos(self):
        return self.__address_infos
    @address_infos.setter
    def address_infos(self, address_infos):
        if not isinstance(address_infos, Address) or address_infos != None:
            print("pas une adresse")
        self.__address_infos = address_infos

    def __str__(self):
        return f"Last name : {self.last_name}\nFirst name : {self.first_name}\nBirth date : {self.birth_date}\nTelephon : {self.num_tel}\nEmail : {self.email}\nAddress : {self.address_infos}"

def main():
    #date = "23.08.1992"
    date = datetime.datetime.strptime("22.08.1992", "%d.%m.%Y")
    tel = "0244455902"
    email = "luca.ray@pm.me"

    street = "Sous la Loge"
    street_num = 5
    zip_code = 1442
    city = "Montagny-près-Yverdon"

    address = Address(street, street_num, zip_code, city)
    person = Person("Ray", "Luca", date, tel, email, address)
    print(person)

    person.address_infos.street_num = 22

    print(person)

    
    

main()