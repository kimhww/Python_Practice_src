i = 0

while True:
    print("{}번째 반복문".format(i))
    i += 1

    input_text = input("> 종료하겠소?(y/n): ")
    
    if input_text in ["y", "Y"]:
        print("반복 종료")
        break