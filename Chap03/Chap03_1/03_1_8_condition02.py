num = input("정수 입력: ")

last_character = num[-1]
a = last_character

if(a in "2468"):
    print("짝수")
if(a in "13579"):
    print("홀수")