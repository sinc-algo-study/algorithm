def move_dice(cmd, dice):
    a, b, c, d, e, f = dice
    if cmd == 1:  # 동쪽
        dice = [d, b, a, f, e, c]
    elif cmd == 2:  # 서쪽
        dice = [c, b, f, a, e, d]
    elif cmd == 3:  # 북쪽
        dice = [e, a, c, d, f, b]
    else:  # 남쪽
        dice = [b, f, c, d, a, e]
    return dice


def copy_dice_number(nx, ny, dice):
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]
    else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0


def solution(n, m, sx, sy):
    def inside_border(nx, ny):
        return 0 <= nx < n and 0 <= ny < m

    x, y = sx, sy
    dice = [0] * 6

    for cmd in cmds:
        nx = x + dx[cmd - 1]
        ny = y + dy[cmd - 1]

        if not inside_border(nx, ny):
            continue

        dice = move_dice(cmd, dice)
        copy_dice_number(nx, ny, dice)
        x, y = nx, ny

        print(dice[0])


if __name__ == '__main__':
    N, M, SX, SY, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    cmds = list(map(int, input().split()))

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    solution(N, M, SX, SY)
