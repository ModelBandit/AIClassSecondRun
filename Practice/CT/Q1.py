import pandas
from datetime import datetime
import calendar

MovieDict = dict()
today = datetime.today()
column = {
    'A' : "O",
    'B' : "O",
    'C' : "O",
    'D' : "O",
    'E' : "O",
}
index  = range(1,6)
df = pandas.DataFrame(column, index=index)


def show_date():
    print(f"Today: {today}")

    # 일요일부터 시작하는 달력
    text_calendar = calendar.TextCalendar(6)

    #이번달 달력
    text_calendar.prmonth(today.year, today.month, w=5, l=2)
    
    #만약 12가 넘어가면
    if(today.month >= 12): # 다음년도 1월 달력
        text_calendar.prmonth(today.year+1, 1, w=5, l=2)
    else:#아니면 그냥 다음달 달력
        text_calendar.prmonth(today.year, today.month+1, w=5, l=2)

dateString = ""
def select_date():
    dateString = input("오늘 이후 원하시는 날짜를 입력하시오 (ex - yymmdd): ")

    if len(dateString) > 6 or len(dateString) < 6:
        print("규격에 맞지 않습니다.")
        return None
    elif  dateString.isdigit() == False:
        print("숫자를 쓰십시요.")
        return None
    elif int(dateString[0:2]) < today.year%100 or int(dateString[2:4]) < today.month or int(dateString[4:6]) < today.day:
        print("과거의 날짜에 예약은 불가능합니다.")
    
    if dateString not in MovieDict:
        MovieDict[dateString] = pandas.DataFrame(column, index=index)
    print("날짜 설정 완료")
    return dateString

def show_seats():	#현재 좌석 현황을 화면에 보여주기 (O, X 표시)
    print(MovieDict[dateString])

def select_seat():	#사용자로부터 예매할 좌석 입력받기
    strings = input("좌석을 입력하시오(ex A1 B3)").split(" ")
    for string in strings:
        if ord(string[0]) < ord('A') or ord(string[0]) > ord('E') or string[0].isdigit() == True or string[1].isdigit() == False:
            print(f"{string} - 해당 좌석은 존재하지 않습니다.")
            return None
        elif check_seat_availability(string):
            print(f"해당 좌석은 다른 고객에게 예약되었습니다")
            return None
    return strings

def check_seat_availability(seat:str):	#좌석이 예매 가능한지 확인하기
    if MovieDict[dateString].loc[int(seat[1]), seat[0]] == 'X':
        return True
    return False

def book_seat(seat, price):	#좌석을 예매하고 금액 계산하기
    print(f"결제금액은 {price} X {len(seat)}로 총 {price * len(seat)}입니다.")
    confirm = input("1. 결제 2. 취소\n")
    if confirm.isdigit() == False and (int(confirm) > 2 or int(confirm) < 1):
        print(f"{confirm} - 입력거부, 결제가 취소됩니다.")
        return 
    
    for s in seat:
        MovieDict[dateString].loc[int(s[1]), s[0]] = 'X'
    print("결제가 완료되었습니다.")


def calculate_price(day_type):	#평일/주말에 따라 가격 계산하기
    if is_weekend(day_type):
        return 12000
    else:
        return 10000
    
def is_weekend(day):	#입력받은 날짜가 주말인지 판단하기
    if day >= 5:
        return True
    return False
    

while True:
    show_date()
    dateString = select_date()
    
    if(dateString == None):
        print("거 잘 좀 쳐 보십쇼")
        continue

    show_seats()

    count = select_seat()
    if(count == None):
        print("거 잘 좀 쳐 보십쇼")
        continue
    price = calculate_price(today.weekday())

    book_seat(count, price)

