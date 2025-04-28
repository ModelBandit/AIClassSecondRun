import pandas
from datetime import datetime
import calendar

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

def show_seats():	#현재 좌석 현황을 화면에 보여주기 (O, X 표시)
    print(df)

def select_date():
    dateString = input("오늘 이후 원하시는 날짜를 입력하시오: ").split()

    strings = input("좌석을 입력하시오(ex A1 B3)").split(" ")
    for string in strings:
        check_seat_availability(string)

def check_seat_availability(seat:str):	#좌석이 예매 가능한지 확인하기
    if df[seat[0]][int(seat[1])] == 'O':
        return True
    return False


def book_seat(seat, price):	#좌석을 예매하고 금액 계산하기
    pass

#date 필요
def calculate_price(day_type):	#평일/주말에 따라 가격 계산하기
    pass

def is_weekend(day):	#입력받은 날짜가 주말인지 판단하기
    pass

while True:
    print(f"Today: {today}")
    show_seats()
    select_seat()

