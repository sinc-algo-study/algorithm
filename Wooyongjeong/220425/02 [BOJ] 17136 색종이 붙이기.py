"""
반복문을 돌다 1을 만나면
-> 5x5, 4x4, ..., 1x1 순으로 확인하여 붙일 수 있는 건 붙이고 넘어가는 방식으로 백트래킹
"""


def in_range(x: int, y: int) -> bool:
    return 0 <= x < SIZE and 0 <= y < SIZE


def check(x: int, y: int, size: int) -> bool:
    for i in range(x, x + size):
        for j in range(y, y + size):
            if not in_range(i, j) or board[i][j] != 1:
                return False
    return True


def papering(x: int, y: int, size: int, flag: int) -> None:
    for i in range(x, x + size):
        for j in range(y, y + size):
            board[i][j] = flag


def dfs(x: int, y: int, cnt: int) -> None:
    global ans

    if ans <= cnt:
        return

    if x >= SIZE - 1 and y > SIZE - 1:
        ans = min(ans, cnt)
        return

    if y >= SIZE:
        dfs(x + 1, 0, cnt)
        return

    if board[x][y] == 1:
        for size in range(5, 0, -1):
            if paper[size] > 0 and check(x, y, size):
                # 색종이 붙여보기
                papering(x, y, size, ATTACH)
                paper[size] -= 1
                # 다음으로
                dfs(x, y + 1, cnt + 1)
                # 색종이 떼기
                papering(x, y, size, DETACH)
                paper[size] += 1
    else:
        dfs(x, y + 1, cnt)


if __name__ == '__main__':
    ATTACH = 0
    DETACH = 1
    SIZE = 10
    INF = int(1e9)
    board = [
        list(map(int, input().split()))
        for _ in range(SIZE)
    ]
    paper = {i: 5 for i in range(1, 6)}
    ans = INF
    dfs(0, 0, 0)
    print(ans if ans != INF else -1)
