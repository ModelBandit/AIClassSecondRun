from SmartPhone import SmartPhone

class SmartPhoneMain:
    def __init__(self):
        self.smartphone = SmartPhone()

    def print_menu(self):
        print("\n주소관리 메뉴")
        print("-----------------------")
        print("1. 연락처 등록")
        print("2. 모든 연락처 출력")
        print("3. 연락처 검색")
        print("4. 연락처 삭제")
        print("5. 연락처 수정")
        print("6. 프로그램 종료")
        print("-----------------------")

    def start(self):
        while True:
            self.print_menu()
            choice = input("원하는 작업을 선택하세요(1~6): ")

            if choice == '1':
                addr = self.smartphone.input_addr_data() # Addr 반환 함수
                self.smartphone.add_addr(addr) # 인자 Addr

            elif choice == '2':
                self.smartphone.print_all_addr() # print all

            elif choice == '3':
                name = input("검색할 이름을 입력하세요: ")
                self.smartphone.search_addr(name) # print
            
            elif choice == '4':
                name = input("삭제할 이름을 입력하세요: ")
                self.smartphone.delete_addr(name)
            
            elif choice == '5':
                name = input("수정할 이름을 입력하세요: ")
                print("새로운 연락처 정보를 입력하세요.")
                new_addr = self.smartphone.input_addr_data() # 추가함수 중복
                self.smartphone.edit_addr(name, new_addr) # 수정함수
            elif choice == '6':
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 선택하세요.")

phone = SmartPhoneMain()
phone.start()