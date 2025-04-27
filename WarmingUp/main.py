# 자원기반 주문가능 여부 반환
def is_resource_sufficient(order_ingredients):
    for key in order_ingredients:
        if resources[key] < order_ingredients[key]:
            return False
    return True

# 계산을 위해 투입된 동전의 총액 반환
def process_coins():
    menuPrice = 0
    CoinList = {"quarters", "dimes", "nickels", "pennies"}
    
    for i, j in zip(coins, CoinList):
        print(f"{j} - {i}", end=" ")
    print(" → ", end="")
    for i, j in zip(coins, CoinInfo):
        if int(i) > 1:
            print(f"{j} X {i}", end=" ")
        elif int(i) <= 1:
            print(f"{j}", end=" ")
    print()

    for i, j in zip(coins, CoinInfo):
        menuPrice += int(i)*j
    return menuPrice

# 금액 승인여부
def is_transaction_successful(money_received, drink_cost):
    if money_received > drink_cost:
        print(f"가격이 초과되었습니다. 남는 동전을 반환합니다. return: $%.2f" % (pay-price))
    elif money_received < drink_cost:
        print("금액이 부족합니다. 잔금 반환 후 리셋됩니다.")
        return False
    return True

# 재료 차감하고 커피 생성
def make_coffee(drink_name, order_ingredients):
    for key in order_ingredients:
        resources[key] -= order_ingredients[key]
    print(f"{drink_name}가 나왔습니다. 즐겼잖아. 한잔해")

MENU = {
    "espresso" : {
        "ingredients" :{
            "water" : 50,
            "coffee" : 18,
        },
        "cost" : 1.5,
    },
    "latte" : {
        "ingredients" :{
            "water" : 200,
            "milk" : 150,
            "coffee" : 24,
        },
        "cost" : 2.5,
    },
    "cappuccino" : {
        "ingredients" :{
            "water" : 250,
            "milk" : 100,
            "coffee" : 24,
        },
        "cost" : 3.0,
    }
}

profit = 0

resources ={
    "water" : 300,
    "milk" : 200,
    "coffee" : 100
}


userOrder = ""
coins = [0,0,0,0]
price = 0 # 물건가격
CoinInfo=[
    0.25,
    0.1,
    0.05,
    0.01
]

while True:
    userOrder = input("어떤 음료를 원하시나요? (espresso/latte/cappuccino): ")

    if(userOrder == "espresso" or userOrder == "latte" or userOrder == "cappuccino"):
        pass
    elif(userOrder == "report"):
        for key in resources:
            print(f"{key} - {resources[key]}")
        print(f"profit - ${profit}")
        continue
    elif(userOrder == "off"):
        break
    else:
        print("없는 명령입니다.")
        continue
    #자원여부 체크
    
    if is_resource_sufficient(MENU[userOrder]["ingredients"]) == False:
        print("재료가 부족합니다")
        continue
    price = MENU[userOrder]["cost"] # 대충 가격을 넣어줌

    coins = input(f"동전을 투입하십시오. need: ${price} (쿼터:0.25 다임:0.1 니켈:0.05 페니:0.01)\nex) input -> 1 2 1 2\t output -> $0.52\n").split()

    if len(coins) > 4 or coins[0].isdigit() == False or coins[1].isdigit() == False or coins[2].isdigit() == False or coins[3].isdigit() == False:
        print("기기오류 기계를 리셋함")
        continue
    # 문자가 들어갔을때 예외처리 필요함

    #지불된 금액
    pay = process_coins()
    print(f"투입된 금액: {pay}")
    
    if is_transaction_successful(pay, price) == False:
        continue

    profit += price
    make_coffee(userOrder, MENU[userOrder]["ingredients"])