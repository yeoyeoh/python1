##07-02##
##int형은 length으로는 에러

c = "125"
n= len(str(c))
print("길이 : %d" % n)

aa=[1, 2, 3, 4, 5, 6, 7, 8, 9]

print(aa[0:3])
print(aa[2:4])
print(aa[2:])
print(aa[:2])

aa[4:5]=['A', 'B']
print(aa)

