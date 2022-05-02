from sys import stdin

x1, y1, x2, y2, x3, y3, x4, y4 = map(int, stdin.readline().split())


# 선이 교차하는지 확인
def ccw(x1, y1, x2, y2, x3, y3):
    ans = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if ans < 0:
        return -1
    elif ans > 0:
        return 1
    else:
        return 0


print(1 if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) < 0 else 0)
