a = float(input("학점을 입력하시오: "))

if a == 4.5:
    print("신")
elif 4.2 <= a < 4.5:
    print("교수님의 사랑")
elif 3.5 <= a < 4.2:
    print("현 체재의 수호자")
elif 2.8 <= a < 3.5:
    print("일반인")
elif 2.3 <= a < 2.8:
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= a < 2.3:
    print("오락문화의 선구자")
elif 1.0 <= a < 1.75:
    print("불가촉천민")
elif 0.5 <= a < 1.0:
    print("자벌레")
elif 0 < a < 1.0:
    print("플랑크톤")
elif a == 0:
    print("시대를 앞서가는 혁명의 씨앗")