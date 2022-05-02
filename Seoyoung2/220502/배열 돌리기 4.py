from itertools import permutations

N, M, K = map(int, input().split())
o_arr = [list(map(int, input().split())) for _ in range(N)]
order = []
for _ in range(K):
    r, c, s = map(int, input().split())
    order.append((r, c, s))


def rotate(r, c, s):
    x, y = r-s-1, c-s-1
    cnt = 2 * s
    new_arr = [a[:] for a in arr]
    for d in range(s):
        # 시작 좌표 : (x+d, y+d)
        nx, ny = x+d, y+d
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            for n in range(cnt):
                nx += dx
                ny += dy
                new_arr[nx][ny] = arr[nx-dx][ny-dy]
        cnt -= 2
    return new_arr


ans = 5555
for perm in permutations(range(K)):
    arr = [a[:] for a in o_arr]
    for p in perm:
        arr = rotate(*order[p])
    for ar in arr:
        ans = min(ans, sum(ar))
print(ans)