import datetime

now =datetime.datetime.now()

if 3<= now.month <=5 :
    print("이번 달은 {}월로 봄입니다.!".format(now.month))
elif 6<= now.month <=8 :
     print("이번 달은 {}월로 봄입니다.!".format(now.month))
elif 9<=  now.month <= 11 :
     print("이번 달은 {}월로 봄입니다.!".format(now.month))
elif now.month==12 or 1 <= now.month <=2 :
     print("이번 달은 {}월로 봄입니다.!".format(now.month))


