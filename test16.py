i, k, guguLine= 0, 0, ""

for i in range(2, 10):
    guguLine= guguLine+str("# %d단 #" % i)
    print("")

print(guguLine)

for i in range(2, 10):
    guguLine=""
    for k in range(1, 10):
        guguLine =guguLine + str("%2dx%2d=%2d" %(i, k, k*i))

    print(guguLine)