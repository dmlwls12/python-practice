# 숫자 맞추기 게임 (Guess the Number)
# 설명: 컴퓨터가 랜덤으로 1~10 사이 숫자를 정하고, 사용자가 맞추는 게임.

import random

number = random.randint(1, 10)
att = 0

while True:
    insert = int(input("숫자를 입력해보세요: "))
    att += 1

    if insert < number:
        print("아 너무 작다!")
    elif insert > number:
        print("아 너무 크다!")
    else:
        print(f"축하! {att}번의 시도 끝에 정답!")
        break;