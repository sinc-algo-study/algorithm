import sys
input = sys.stdin.readline
from collections import deque

'''
0  1  2  3
4  5  6  7
8  9  10 11
12 13 14 15

0  1  2  3  4  5  6  7
8  9  10 11 12 13 14 15
16 17 18 19 20 21 22 23
24 25 26 27 28 29 30 31
...

n2=(n/2)**2
16이면,
0 1 / 4 5 => 0부터 8/4번째 + 0 더하기 8/2부터 8/2+8/4번째까지  
2 3 / 6 7
8 9 / 12 13
10 11 / 14 15
64이면,
0 1 2 3 / 8 9 10 11 / 16 17 18 19 / 24 25 25 27

1100
0(0101)10
1100
1101
'''

# 2*2씩 담기. 원소가 전부 1인지 또는 0인지 all, any로 체크하기
def check1or0(arr):
    if all(arr):
        return '1'
    elif not any(arr):
        return '0'


def press(id, now, answer):
    now //= 2
    answer += check1or0(video[id:now**2])
    if now
    res = ''
    now//=2
    res += '('
    for i in range(4):

check

        res += ')'

    for i in range(4):
        j=n/2
        que.append(video[i:i + j / 2] + video[i + j:i + j + j / 2])
        while que:
            temp = que.pop()
            if all(temp):
                answer[i]=1
                break
            elif not any(temp):
                answer[i]=0
                break
            j /= 2
            que.append(video[i:i+j/2]+video[i+j:i+j+j/2])





if '__main__' == __name__:
    n = int(input())
    video = []
    if n==1:
        print (int(input()))
    else:
        for _ in range(n/2): # 32 * 32
            temp = list(map(int, list(input().rstrip())))
            temp2 = list(map(int, list(input().rstrip())))
            for i in range(n/2):
                video.append(temp[2*i:2*(i+1)]+temp2[2*i:2*(i+1)])
        now = n
        answer = ''
        answer += press(0, now, answer)
