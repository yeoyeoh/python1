list1=[]
list2=[]
list3=[]
result=""

value=0

for i in range(0, 5):
    for k in range(0, 4):
        value=value+3
        for j in range(1, 10):
            result= ("%d * %d = %d" % (value, j, value * j))
            list1.append(result)
        list2.append(list1)
        list1 = []

    list3.append(list2)
    list2=[]


for i in range(0, 5):
    for k in range(0, 4):
        print("%s" % list3[i][k], end="")
        print("")

print(len(list3))