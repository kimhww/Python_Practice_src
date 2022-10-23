output_a = "{:d}".format(43)

output_b = "{:5d}".format(43)
output_c = "{:10d}".format(43)

output_d = "{:05d}".format(43)
output_e = "{:05d}".format(-43)

print("** 기본 **")
print(output_a)
print("** 특정 칸에 출력 **")
print(output_b)
print(output_c)
print("** 빈공간 0으로 채우기 **")
print(output_d)
print(output_e)