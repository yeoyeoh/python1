##문자열##
ss="파이썬최고"
print(ss[0])
print(ss[1:3])
print(ss[3:])

ss2=ss.replace('파이썬', '클라우드')       #파이썬을 클라우드로 바꾸기
print(ss2)

ip='192.168.0.23'
newip=ip.replace('.', '')
print(newip)

ss3=' AbcD Efg '
ss3=ss3.lower()
if len(ss3) > 5:
    print("아이디를 다시 설정하세요")


ss4=' 달려라 하니 '
print("<" + ss4+ ">")
print("<" + ss4.strip() + ">")