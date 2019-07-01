##09-07##
def func1():
    global a
    a=10
    print("func1()에서 a값 %d" % a)

def func2():
    print("func2()에서 a값 %d" % a)


def telcheck(aa):

    print(aa)
    if len(aa) == 11:
        return True
    else:
        return False


if __name__=="__main__":
    result = False

    tel1='010-4088-01'
    tel2='010-4088-0116'

    #tel1=tel1.replace('-','')
    #result=telcheck(tel1)
    tel2 = tel2.replace('-', '')
    result = telcheck(tel2)

    if result==True:
        print("전화번호 형식에 맞음")
    else:
        print("전화번호 형식에 맞지 않음")