def ccw(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    result = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if result > 0:
        return 1
    elif result < 0:
        return -1
    return 0


def solution(coordinates):
    x1, y1, x2, y2, x3, y3, x4, y4 = coordinates
    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x3, y3)
    p4 = (x4, y4)

    if ccw(p1, p2, p3) * ccw(p1, p2, p4) < 0:
        return 1
    return 0


if __name__ == '__main__':
    coordinates = list(map(int, input().split()))
    print(solution(coordinates))
