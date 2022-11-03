list_a = [0, 1, 2, 3, 4, 5]
print("** 리스트의 요소 하나 제거하기 **")

del list_a[1]
print("del list_a[1]: ", list_a)

list_a.pop(2)
print("pop(2): ", list_a)

#값으로 제거하는 법: remove() -> 중복된 값 중에 첫번째부터 제거
list_1 = [1, 2, 3, 2, 4]
list_1.remove(2)
print("list_1 > ", list_1)

#모두 제거하는 법: clear()
list_2 = [1, 2, 3, 4, 5]
list_2.clear()
print("list_2 > ", list_2)

#리스트 내부에 있는지 확인하는 방법: in/not in 연산자
list_3 = [1, 2, 3, 4, 5]
print(1 in list_3)
print(100 not in list_3)