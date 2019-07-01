##튜플##

tt1=([1, 2, 3], (4, 5, 6), [[7, 8], 9], 10, 20, 30)

print(tt1)

tt3={1: "한국", 2: "USA"}
print(tt3)


tt4={"이름": "홍길동", "주소": "천안", "연령": "20대", "보유차량": ("그랜져", "아반테")}
print(tt4["보유차량"])
#tt4={0: "홍길동", 1: "천안", 2: "20대"}       #key 값 : value 값
#print(tt4[0])

foods={"떡볶이": "오뎅",
       "짜장면": "단무지",
       "라면": "김치",
       "피자": "피클",
       "맥주": "땅콩",
       "치킨": "치킨무",
       "삼겹살": "상추"
       };

while True:
    myfood=input(str(list(foods.keys())) + "중 좋아하는 음식은?")
    if myfood in foods:
        print("<%s> 궁합 음식은 <%s>입니다." % (myfood, foods.get(myfood)))
    elif myfood=="끝":
        break
    else:
        print("존재하지 않습니다.")



import operator

trainDic, trainList={}, {}

trainDic={'Thomas': '토마스',
          'Edward':'에드워드',
          'Henry': '헨리',
          'Gothen': '고든',
          'James': '제임스'
          }


trainList=sorted(trainDic.items(), key=operator.itemgetter(0))

print(trainList)