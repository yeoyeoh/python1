list1=[]
list2=[]

value = 0
for i in range(0, 5):
    for k in range(0, 4):
        value = value + 3
        list1.append(value)

    list2.append(list1)
    list1=[]    

print(list2)

for i in range(0, 5):
    for k in range(0, 4):
        print("%3d" % list2[i][k], end="")
    print()

