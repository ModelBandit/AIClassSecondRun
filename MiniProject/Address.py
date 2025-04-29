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

    def printInfo(self):
        print(f"이름: {self.name}")
        print(f"전화: {self.phone}")
        print(f"이메일: {self.email}")
        print(f"주소: {self.address}")
        print(f"그룹(친구/가족): {self.group}")

class CompanyAddr(Addr):
    def __init__(self,name, phone, email, address, group, company, department, rank):
        super().__init__(name, phone, email, address, group)
        self.__company = company
        self.__department = department
        self.__rank = rank

    @property
    def company(self):
        return self.__company
    @company.setter
    def company(self, value):
        self.__company = value

    @property
    def department(self):
        return self.__department    
    @department.setter
    def department(self, value):
        self.__department = value

    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, value):
        self.__rank = value

    def printInfo(self):
        super().printInfo()
        print(f"회사명: {self.company}")
        print(f"부서: {self.department}")
        print(f"직급: {self.rank}")


class CustomerAddr(Addr):
    def __init__(self, name, phone, email, address, group, business, itemName, rank):
        super().__init__(name, phone, email, address, group)
        self.__business = business
        self.__itemName = itemName
        self.__rank = rank

    @property
    def business(self):
        return self.__business
    @business.setter
    def business(self, value):
        self.__business = value

    @property
    def itemName(self):
        return self.__itemName
    @itemName.setter
    def itemName(self, value):
        self.__itemName = value

    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, value):
        self.__rank = value

    
    def printInfo(self):
        super().printInfo()
        print(f"거래처: {self.business}")
        print(f"품목: {self.itemName}")
        print(f"직급: {self.rank}")