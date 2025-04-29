from Address import *

class SmartPhone:
    def __init__(self):
        self.AddressList = []
        self.groupList = ("친구","가족","회사","거래처")
        num = 2
        print(f"# 데이터 {num}개를 입력합니다.")
        for i in range(num):
            address = self.input_addr_data()
            if address == None:
                continue
            self.add_addr(address)

    def input_addr_data(self):
        name = input("이름: ")
        if name.isdigit() == True:
            print("생성 실패 - 숫자로만 된 이름으로 받지 않습니다.")
            return None
        
        phone = input("전화번호: ")
        if len(phone) < 13 or len(phone) > 13:
            print("생성 실패 - 무조건 13자리 000-1111-2222")
            return None
        for i in range(len(phone)):
            if phone[i].isdigit() == False and phone[i] != '-':
                print("생성 실패 - 숫자나 -를 제외한 값은 거부됨")
                return None

        email = input("이메일: ")
        if email.find('@') == -1 or email.find('.') == -1:
            print("생성 실패 - name@domain.com 같은 일반 이메일 형태만 받습니다.")
            return None

        address = input("주소: ")
        # 예외처리용

        group = input("그룹(친구/가족/회사/거래처): ")
        if group not in self.groupList:
            print("생성 실패 - 설정된 예시 말고는 거부됩니다.")
            return None
        
        addr = 0 # Addr을 초기화할 공간
        if group == "회사":
            company = input("회사명: ")
            if company.isdigit() == True:
                print("생성 실패 - 숫자로만 된 이름으로 받지 않습니다.")
                return None

            department = input("품목명: ")
            if department.isdigit() == True:
                print("생성 실패 - 숫자로만 된 이름으로 받지 않습니다.")
                return None
            
            rank = input("직급: ")
            if rank.isdigit() == True:
                print("생성 실패 - 숫자로만 된 이름으로 받지 않습니다.")
                return None

            addr = CompanyAddr(name, phone, email, address, group, company, department, rank)
        elif group == "거래처":
            
            business = input("거래처: ")
            if business.isdigit() == True:
                print("생성 실패 - 숫자로만 된 이름으로 받지 않습니다.")
                return None

            itemName = input("품목명: ")
            if itemName.isdigit() == True:
                print("생성 실패 - 숫자로만 된 이름으로 받지 않습니다.")
                return None
            
            rank = input("직급: ")
            if rank.isdigit() == True:
                print("생성 실패 - 숫자로만 된 이름으로 받지 않습니다.")
                return None

            addr = CustomerAddr(name, phone, email, address, group, business, itemName, rank)
        else:
            addr = Addr(name, phone, email, address, group)

        return addr

    def add_addr(self, addr:Addr):
        if addr == None:
            print("생성 실패")
            return
        
        self.AddressList.append(addr)
        print(f"데이터가 저장되었습니다. ({len(self.AddressList)})")

    
    def print_addr(self, index:int):
        if index < 0 or index >= len(self.AddressList):
            print("범위를 초과하였습니다.")
            return
        
        self.AddressList[index].printInfo()
        print()

    def print_all_addr(self):
        for i in range(len(self.AddressList)):
            self.print_addr(i)

    def search_addr(self, name:str):
        index = self.find_addr_index(name)
        if index == None:
            print(f"{name} - 대상이 발견되지 않았습니다.")
        else:
            self.print_addr(index)
        

    def delete_addr(self, name:str):
        index = self.find_addr_index(name)
        if index == None:
            print(f"{name} - 대상이 발견되지 않았습니다.")
        else:
            self.AddressList.pop(index)
            print(f"{name} - 대상이 제거되었습니다.")

    def edit_addr(self, name:str, newAddr:Addr):
        index = self.find_addr_index(name)

        if index == None:
            print(f"{name} - 대상이 발견되지 않았습니다.")
        elif newAddr == None:
            print(f"새 데이터 생성 실패 - 수정 취소")
        else:
            self.AddressList.pop(index)
            self.AddressList.insert(index, newAddr)
    
    def find_addr_index(self, name:str):
        for i in range(len(self.AddressList)):
            if self.AddressList[i].name == name:
                return i
        return None
    
