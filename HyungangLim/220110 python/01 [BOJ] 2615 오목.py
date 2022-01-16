def dfs(color, dept, r, c, d):
    global finish, winner_color, winner_row, winner_col

    if dept >= 5:
        if dept == 5:  # 오목 완성
            finish = True
            winner_color = color
            winner_row = r
            winner_col = c
        else:  # 육목은 승리 조건이 아니다
            finish = False

    nr = r + r_list[d]
    nc = c + c_list[d]
    if not (-1 < nr < N and -1 < nc < N): return
    if board[nr][nc] != board[r][c] or check[nr][nc][d]: return
    dfs(color, dept + 1, nr, nc, d)

    # winner 좌표 체크
    if dept == 1 and finish:
        if winner_col != c:
            if winner_col > c:
                winner_row = r
                winner_col = c
        else:
            if winner_row > r:
                winner_row = r
                winner_col = c


def solution():
    for i in range(N):
        for j in range(N):
            for k in range(8):
                if board[i][j] == 0 or check[i][j][k]: continue
                dfs(board[i][j], 1, i, j, k)

                if finish:
                    print(winner_color)
                    print(str(winner_row + 1) + " " + str(winner_col + 1))
                    return


if __name__ == '__main__':
    N = 19
    board = [list(map(int, input().split())) for _ in range(N)]
    check = [[[False] * 8 for _ in range(N)] for _ in range(N)]

    finish = False
    winner_color = 0
    winner_row = 0
    winner_col = 0

    r_list = [-1, 1, 0, 0, -1, -1, 1, 1]
    c_list = [0, 0, -1, 1, 1, -1, -1, 1]

    solution()
