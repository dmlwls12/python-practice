board = []

while True:
    print("\n1. 할 일 추가 \n2. 리스트 불러오기 \n3. 할 일 삭제 \n4. 프로그램 종료")
    choice = input("메뉴를 선택하세요: ")

    if choice == "1":
        content = input("할 일: ")
        board.append(content)
    elif choice == "2":
        if not board:
            print("리스트가 비어있습니다. 입력해주세요.")
        else:
            for idx, task in enumerate(board, 1):
                print(f"{idx}. {task}")
    elif choice == "3":
        if not board:
            print("리스트가 비어있습니다.")
        else:
            for i, content in enumerate(board, 1):
                print(f"{i}. {content}")
            num = int(input("번호를 선택하세요: "))
            board.pop(num - 1)
            print("삭제되었습니다.")
    elif choice == "4":
        print("프로그램을 종료합니다.")
        break
    else:
        print("없는 번호입니다. 다시 선택하세요.")
