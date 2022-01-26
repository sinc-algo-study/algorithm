'''

N이 작으니까 브루트 포스

놓을 수 있으면 놓고(재귀) 안 되면 다음 좌표 검사

퀸의 이동 방향은 3가지 : 행 이동, 열 이동, 대각 이동
1. 행 이동은 검사할 필요 없다
-> 어차피 한 행에 하나의 퀸만 가능. 퀸을 놓는 데 성공하면 break 한 후 다음 행을 검사할 것임
2. 열 이동은 내 위로만 보면 된다
-> [0][0] ~ [N][N] 좌표를 순서대로 볼 것. 즉, 위에서부터 검사하며 내려온다. 아래에는 어차피 놓인 퀸이 없다.
3. 대각 이동은 상단만 본다.
-> 열 이동과 마찬가지. 상단 좌/우측 대각선만 보면 된다.

'''


def is_possible(r, c):
    # 열이동
    pr = r - 1  # 열이동은 행을 체크한다
    while pr >= 0:
        if board[pr][c]:
            return False
        pr -= 1

    # 대각 이동 1 (좌)
    pr = r - 1
    pc = c - 1
    while pr >= 0 and pc >= 0:
        if board[pr][pc]:
            return False
        pr -= 1
        pc -= 1

    # 대각 이동 2 (우)
    pr = r - 1
    pc = c + 1
    while pr >= 0 and pc < N:
        if board[pr][pc]:
            return False
        pr -= 1
        pc += 1

    return True


def dfs(r, c, dept):  # c는 안 쓰지만 없으니 뭔가 불안..
    global ans
    if dept == N:
        ans += 1
        return

    for i in range(r+1, N):
        for j in range(N):
            if is_possible(i, j):
                board[i][j] = 1
                dfs(i, j, dept+1)
                board[i][j] = 0


def solution():
    for i in range(N):
        for j in range(N):
            board[i][j] = 1
            dfs(i, j, 1)
            board[i][j] = 0


if __name__ == '__main__':
    ans = 0
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    solution()
    print(ans)