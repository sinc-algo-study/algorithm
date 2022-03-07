import sys
input = sys.stdin.readline

'''
전에 풀어봤던 거랑 똑같음 => 응 시간초과~
'''

def oneTry():
    flag = True
    while flag:
        if bombStr in givenStr:
            givenStr = givenStr.replace(bombStr, "")
        else:
            flag = False
    if givenStr == "":
        return "FRULA"
    else:
        return givenStr

'''
replace 대신 시간복잡도 O(1)인 stack 사용
'''
def again():
    ret = givenStr[:lengBomb-1]
    for i in range(lengBomb-1, lengGiven):
        ret.append(givenStr[i])
        if ret[-lengBomb:]==bombStr:
            ret[-lengBomb:]=[]
    if ret:
        return "".join(ret)
    else:
        return "FRULA"


if "__main__" == __name__:
    givenStr = list(input().strip())
    bombStr = list(input().strip())
    lengGiven = len(givenStr)
    lengBomb = len(bombStr)
    # print(oneTry())
    print(again())



