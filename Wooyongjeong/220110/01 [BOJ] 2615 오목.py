"""
1. 문제를 꼼꼼하게 읽지 않은 채로, 각 바둑알마다 8방향 검사해서
    -> 같은 색 바둑알이 연속으로 다섯 알이면 이긴 걸로 판단하려고 했음
2. 문제에 '여섯 알 이상이 연속적으로 놓인 경우에는 이긴 것이 아니다.'
3. 그럼 다섯 알을 체크하고 -> 육목인지 아닌지 확인
    -> 즉, 오목이라면 시작지점에서 반대방향으로 한 칸 간 거
        + 오목이라고 체크한 곳(다섯번째)에서 한 칸 더 간 거
        둘 다 빈 칸 or 다른 색깔이어야 이긴 거로 판정
4. 그리고 8방향을 모두 검사하면 안됨
    -> ↓, ⬊, ➞, ⬈ 네 방향만 검사하면 됨
"""


def check(x, y, color):
    if 0 <= x < N and 0 <= y < N and board[x][y] == color:
        return True
    return False


def is_6mok(x, y, nx, ny, i):
    if check(x - dx[i], y - dy[i], board[x][y]) \
            or check(nx + dx[i], ny + dy[i], board[nx][ny]):
        return True
    return False


def is_5mok(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        count = 1

        while check(nx, ny, board[x][y]):
            count += 1

            if count == 5:
                if is_6mok(x, y, nx, ny, i):
                    break
                return True

            nx += dx[i]
            ny += dy[i]

    return False


def solution(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0 and is_5mok(i, j):
                print(board[i][j])
                print(i + 1, j + 1)
                return
    print(0)


if __name__ == '__main__':
    N = 19
    board = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, 1, 0, -1]  # ↓, ⬊, ➞, ⬈
    dy = [0, 1, 1, 1]
    solution(board)
