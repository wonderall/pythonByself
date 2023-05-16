import datetime

now = datetime.datetime.now()

if now.hour < 12 :
    print("현재 시각은 {}시 오전입니다.!".format(now.horu))
if now.hour >= 12 :
    print("현재 시각은 {}시 오후입니다.!".format(now.hour))