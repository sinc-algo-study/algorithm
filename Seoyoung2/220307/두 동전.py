from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
board = [list(stdin.readline().rstrip()) for _ in range(N)]


def is_out(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return True
    return False


def bfs(q):
    check[cx1][cy1][cx2][cy2] = 0
    while q:
        x1, y1, x2, y2 = q.popleft()
        if check[x1][y1][x2][y2] >= 10:
            return -1
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx1, ny1 = x1 + dx, y1 + dy
            nx2, ny2 = x2 + dx, y2 + dy
            if is_out(nx1, ny1) and is_out(nx2, ny2):
                continue
            if is_out(nx1, ny1):
                return check[x1][y1][x2][y2] + 1
            if is_out(nx2, ny2):
                return check[x1][y1][x2][y2] + 1
            if board[nx1][ny1] == '#':
                nx1, ny1 = x1, y1
            if board[nx2][ny2] == '#':
                nx2, ny2 = x2, y2
            if check[nx1][ny1][nx2][ny2] == -1:
                check[nx1][ny1][nx2][ny2] = check[x1][y1][x2][y2] + 1
                q.append((nx1, ny1, nx2, ny2))
    return -1


(cx1, cy1), (cx2, cy2) = [(x, y) for x in range(N) for y in range(M) if board[x][y] == 'o']
check = [[[[-1] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
q = deque([(cx1, cy1, cx2, cy2)])
print(bfs(q))
