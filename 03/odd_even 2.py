number = input("정수 입력 > ")

last_character = number[-1]

if last_character in "0248" :
    print("짝수 입니다.")
else :
    print("홀수 입니다.")