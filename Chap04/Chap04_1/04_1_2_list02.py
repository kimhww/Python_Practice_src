list_a = [1, 2, 3]

print("** 리스트 뒤에 요소 추가하기 **")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

print("** 리스트 중간에 요소 추가하기 **")
list_a.insert(0,10)
print(list_a)

#추가적으로 extend(), append(), insert()는 파괴적으로 원본에 직접적으로 영향을 줌
list_1 = [1, 2]
list_1.extend([3,4])
print(list_1)