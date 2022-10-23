import datetime


now = datetime.datetime.now()

if 2 < now.month <= 5:
    print("이번 달은 {}월로 봄".format(now.month))

if 5 < now.month <= 8:
    print("이번 달은 {}월로 여름".format(now.month))

if 8 < now.month <= 11:
    print("이번 달은 {}월로 가을".format(now.month))

if 11 < now.month <= 2:
    print("이번 달은 {}월로 겨울".format(now.month))