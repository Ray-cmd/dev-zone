class Address():
    def __init__(self, street, street_num, zip_code, city):
        self.street = street
        self.street_num = street_num
        self.zip_code = zip_code
        self.city = city

    @property
    def street(self):
        return self.__street
    @street.setter
    def street(self, street):
        if not isinstance(street, str):
            raise ValueError("Street must be a string")
        for char in street:
            if char != " " and not char.isalpha():
                raise ValueError("Street must be characters")
        if len(street) < 3 or len(street) > 64:
            raise ValueError("Street must be between 3 and 64 characters")
        self.__street = street

    @property
    def street_num(self):
        return self.__street_num
    @street_num.setter
    def street_num(self, street_num):
        if not isinstance(street_num, int):
            raise ValueError("Street number must be an integer")
        if len(str(street_num)) > 2:
            raise ValueError("Street number canont be longer than 2 digits")
        if street_num < 1:
            raise ValueError("Street number canont be lower than 1")
        self.__street_num = street_num

    @property
    def zip_code(self):
        return self.__zip_code
    @zip_code.setter
    def zip_code(self, zip_code):
        if not isinstance(zip_code, int):
            raise ValueError("Zip code must be an integer")
        if len(str(zip_code)) != 4 :
            raise ValueError("Swiss zip code are 4 digits long")
        self.__zip_code = zip_code

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city):
        if not isinstance(city, str):
            raise ValueError("City must be a string")
        if len(city) < 3 or len(city) > 64:
            raise ValueError("City must be between 3 and 64 characters")
        self.__city = city

    def __str__(self):
        return f"{self.street} {self.street_num} {self.zip_code} {self.city}"