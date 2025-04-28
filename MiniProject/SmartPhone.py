from Address import Addr

class SmartPhone:
    def __init__(self):
        self.AddressList = []
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
            print("생성 실패 - 숫자는 이름으로 받지 않습니다.")
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

        group = input("그룹(친구/가족): ")
        if group != "친구" and group != "가족":
            print("생성 실패 - 친구나 가족만 받습니다.")
            return None

        addr = Addr(name, phone, email, address, group)
        return addr

    def add_addr(self, addr:Addr):
        if addr == None:
            print("생성 실패")
            return
        
        self.AddressList.append(addr)
        print(f"데이터가 저장되었습니다. ({len(self.AddressList)})")

    
    def print_addr(self, index:int):
        if iter < 0 or iter >= len(self.AddressList):
            print("범위를 초과하였습니다.")
            return
        
        print(f"이름: {self.AddressList[index].name}")
        print(f"전화번호: {self.AddressList[index].phone}")
        print(f"이메일: {self.AddressList[index].email}")
        print(f"주소: {self.AddressList[index].address}")
        print(f"그룹(친구/가족): {self.AddressList[index].group}")
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
    
