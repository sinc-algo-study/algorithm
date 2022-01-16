# https://www.acmicpc.net/problem/2615

from sys import stdin

board = [list(map(int, stdin.readline().split())) for _ in range(19)]
# 방향별로 방문 체크 필요
check = [[[False] * 4 for _ in range(19)] for _ in range(19)]


def check_result(x, y, color):
    dxdy = [(0, 1), (1, 0), (-1, 1), (1, 1)] # 우, 하, 우상, 우하
    for d in range(4):
        if check[x][y][d]:
            continue
        check[x][y][d] = True

        nx, ny = x, y
        cnt = 1
        while True:
            nx += dxdy[d][0]
            ny += dxdy[d][1]
            if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color and not check[nx][ny][d]:
                cnt += 1
                check[nx][ny][d] = True
            else:
                break
        if cnt == 5:
            return True
    return False


for j in range(19):
    for i in range(19):
        if board[i][j] != 0 and not all(check[i][j]):
            if check_result(i, j, board[i][j]):
                print(board[i][j])
                print(i+1, j+1)
                exit(0)
print(0)

