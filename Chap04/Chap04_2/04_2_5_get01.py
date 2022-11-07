dic = {
    "name" : "7D 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕"],
    "origin" : "필리핀"
}

value = dic.get("존재하지 않는 키")
print("값: ", value)

if value == None:
    print("존재하지 않는 키에 접근했어요")