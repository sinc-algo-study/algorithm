import collections
import sys
sys.setrecursionlimit(10**6)


def dfs(x, y, n, board, island_number):
    board[x][y] = island_number
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
            dfs(nx, ny, n, board, island_number)


def bfs(n, board, island_number):
    q = collections.deque()
    for i in range(n):
        for j in range(n):
            if board[i][j] == island_number:
                q.append((i, j))

    cost = 0
    visited = [[False] * n for _ in range(n)]
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if visited[nx][ny]:
                        continue
                    if board[nx][ny] > 0 and board[nx][ny] != island_number:
                        return cost
                    if board[nx][ny] == 0:
                        visited[nx][ny] = True
                        q.append((nx, ny))
        cost += 1
    return cost


def solution(n, board):
    island_number = 2
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                dfs(i, j, n, board, island_number)
                island_number += 1

    result = INF
    for number in range(2, island_number):
        result = min(result, bfs(n, board, number))
    return result


if __name__ == '__main__':
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    INF = int(1e9)
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, board))
