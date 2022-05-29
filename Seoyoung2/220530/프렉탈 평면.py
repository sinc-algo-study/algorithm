from math import pow

s, n, k, r1, r2, c1, c2 = map(int, input().split())

entire = int(pow(n, s))      # 전체 배열 한변의 길이


# 현재 좌표가 가운데 인지,, (가운데면 black, 가운데 아니면 white)
def get_color(width, x, y):
    if width == 1:
        return 0

    # nxn 등분해서 다시 탐색
    w = width // n

    # nxn 배열의 가운데 위치인지 확인
    if w * (n-k)//2 <= x < w * (n+k)//2 and w * (n-k)//2 <= y < w * (n+k)//2:
        return 1

    return get_color(w, x % w, y % w)


for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        print(get_color(entire, i, j), end="")
    print()