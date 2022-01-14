import sys
#가로, 세로, 회전수
n, m, r = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

def rotate(m,n,arr):
    tempArr = [[0 for i in range(m)] for _ in range(n)]
    for y in range(1,n+1):
        for x in range(1,m+1):
            # 좌
            if y<x and y<=(-x+m+1) and y<=int(n/2):
                tempArr[y-1][x-2]=arr[y-1][x-1]
            # 상
            elif x>(int(m/2)+m%2) and y>(-x+m+1) and y<=(x-m+n):
                tempArr[y-2][x-1]=arr[y-1][x-1]
            # 우
            elif y>(int(n/2)+n%2) and y>=(n-x+1) and y>(x-m+n):
                tempArr[y-1][x]=arr[y-1][x-1]
            # 하
            else :
                tempArr[y][x-1]=arr[y-1][x-1]
    arr = tempArr
    return arr

for _ in range(r):
    arr = rotate(m,n,arr)

for y in range(n):
    print(' '.join(map(str,arr[y])))