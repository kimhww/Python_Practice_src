import datetime

now = datetime.datetime.now()

if now.hour < 12:
    print("현재 시각은 오전 {}시입니다.".format(now.hour))

if now.hour >= 12:
    print("현재 시각은 오후 {}시 {}분입니다.".format(now.hour-12, now.minute))