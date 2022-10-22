a = "Hello Python Programming...!"
print(a.upper()) #대문자로
print(a.lower()) #소문자로

b = """
  안녕 난 김현우야
"""

print(b)
print(b.strip()) #공백지우기

c = "TrainA10"
print(c.isalnum())
print("10".isdigit())
print("ten".isdigit())

d = "hi hi my name is Hyeonwoo"
print(d.find("hi")) #문자열 찾기(위치)
print(d.rfind("hi"))

print("hi" in d) #in 연산자는 포함하고 있는지에 대해 알 수 있음
print("hello" in  d)

e = "hi my name is"
print(e.split(" ")) #()안의 문자열의 기준으로 자름