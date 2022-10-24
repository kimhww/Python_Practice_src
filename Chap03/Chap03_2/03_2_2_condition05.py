import datetime

now = datetime.datetime.now()
m = now.month

if 3<= m <=5:
    print("봄")
elif 6<= m <= 8:
    print("여름")
elif 9<= m <= 11:
    print("가을")
else:
    print("겨울")