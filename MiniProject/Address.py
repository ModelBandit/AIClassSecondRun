class Addr:
    def __init__(self, name, phone, email, address, group):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__address = address
        self.__group = group

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, value):
        self.__phone = value
    
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def group(self):
        return self.__group
    @group.setter
    def group(self, value):
        self.__group = value