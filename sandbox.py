dict_test = {}
dict_test["hello"] = 1
print(dict_test)
dict_test["hello"] += 1

print(dict_test)


dict_test["dictionary value"] = {"item 1": 3, "list_item": [1, 2, 3, 4, 5]}

for i, j in dict_test:
    print(i)
    print(j)
