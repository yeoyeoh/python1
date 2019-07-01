mySet1={1, 2, 3, 4, 5}
mySet2={4, 5, 6, 7}
print(mySet1 & mySet2)     #교집합
print(mySet1 | mySet2)     #합집합
print(mySet1 - mySet2)    #차집합
print(mySet1 ^ mySet2)     #대칭 차집합

##컴프리헨션##
numList=[]
for num in range(1, 6):
    numList.append(num)

print(numList)

numList2=[num for num in range(1, 6)]
print(numList2)

##리스트 복사##
oldList=['짜장면', '탕수육', '군만두']
#주소를 같이 사용 / 메모리 같이 사용 / 내용 같음
#newList=oldList

#주소 따로 사용/ 내용이 다름
newList=[]
newList=oldList[:]
print(newList)
oldList[0]='짬뽕'
oldList.append('깐풍기')
print(newList)
print(oldList)