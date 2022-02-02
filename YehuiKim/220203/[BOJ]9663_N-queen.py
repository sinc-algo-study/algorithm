import sys
in_put = sys.stdin.readline


def check_queens(x,y):
    for cx,cy in queens:
        if cx==x or abs(cx-x)==abs(cy-y):
            if cy==y:
                continue
            else :
                return False
    return True


def put_queen(y):
    global ans
    if y==n:
        ans += 1
        queens.pop()
    else :
        for x in range(n):
            queens.append((x,y))
            if check_queens(x,y):
                put_queen(y+1)
            else :
                queens.pop()
        if queens:
            queens.pop()


if '__main__' == __name__:
    n = int(in_put())
    queens = []
    ans = 0
    put_queen(0)
    print(ans)