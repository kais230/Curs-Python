list=[7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# 1)
list_ord1=sorted(list)
print(list_ord1)

# 2)
list_ord2=list
list_ord2 = sorted(list,reverse=True)
print(list_ord2)

# 3)
print(sorted(list)[1::2])

#4)
print(sorted(list)[0::2])

#5)

for i in range(len(list)):
    if (list[i] % 3 == 0):
        print(list[i])







