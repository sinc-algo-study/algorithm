from sys import stdin
from collections import deque

N, M, R = map(int, stdin.readline().split())
A = [list(map(int, stdin.readline().split())) for _ in range(N)]
dxdy = (1, 0), (0, 1), (-1, 0), (0, -1)

# 2차원 배열 -> 1차원 배열 L개
L = min(N, M) // 2
T = [deque() for _ in range(L)]

for t in range(L):
    # 시작 좌표, 끝 좌표
    sx, sy, ex, ey = t, t, N-t-1, M-t-1

    # 2차원 배열 -> 1차원 배열
    x, y = sx, sy
    for dx, dy in dxdy:
        while True:
            if sx <= x+dx <= ex and sy <= y+dy <= ey:
                x += dx
                y += dy
                T[t].append(A[x][y])
            else:
                break

    # R번 반시계 방향 회전
    T[t].rotate(R)
    # T[t] = T[t][-R:] + T[t][:-R]

    # 1차원 배열 -> 2차월 배열
    for dx, dy in dxdy:
        while True:
            if sx <= x+dx <= ex and sy <= y+dy <= ey:
                x += dx
                y += dy
                A[x][y] = T[t].popleft()
            else:
                break

for a in A:
    print(*a)
