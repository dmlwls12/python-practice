records = []

def record():
    ammount = int(input("얼마입니까?: "))
    type = input("수입/지출: ")

    records.append({"amount": ammount, "type": type})
    print("")

def balance():
    balance = 0
    for r in records:
        if r["type"] == "수입":
            balance += r["amount"]
        elif r["type"] == "지출":
            balance -= r["amount"]
        else:
            balance
    print(f"잔액: {balance} 원 입니다.")

while True:
    print("\n1. 장부 기입 \n2. 잔고 출력 \n3. 프로그램 종료")
    selection = input("필요한 활동을 선택하세요: ")

    if selection == "1":
        record()
    elif selection == "2":
        balance()
    elif selection == "3":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")


