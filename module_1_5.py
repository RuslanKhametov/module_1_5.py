immutable_var = 1, 2, 3, True, "Дождливое лето"
print(immutable_var)
immutable_var [2]=200 #не поддерживает обращение по элементам

mutable_list = [1, 2, 3, True, "Дождливое лето"]
print(mutable_list)
mutable_list[0]=400
print(mutable_list)
mutable_list[3]=False
print(mutable_list)
mutable_list[4]='у меня всё получится'
print(mutable_list)
mutable_list.remove(2)
print(mutable_list)
print(1 in mutable_list)
print(400 in mutable_list)
mutable_list.append('домашняя работа готова')
print(mutable_list)