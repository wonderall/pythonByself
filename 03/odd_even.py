number = input("정수 입력 > ")

last_character = number[-1]

last_number = int(last_character)

if (last_number%2) == 0 :
    print("짝수 입니다.")
else :
    print("홀수 입니다.")