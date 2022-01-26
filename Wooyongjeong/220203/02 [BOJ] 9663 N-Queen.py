def check(c):
    for r in range(c):
        if col[r] == col[c] or abs(col[c] - col[r]) == c - r:
            # 같은 행에 다른 퀸이 있거나, 대각선 방향에 다른 퀸이 있으면 False
            return False
    # 같은 열에 다른 퀸이 있는 경우는 없으므로 True
    return True


def solve(c):
    global answer
    if c == N:
        # 모든 열에 퀸을 위치하고(N개), 서로 공격할 수 없는 상태인 경우
        answer += 1
        return
    for r in range(N):
        # c번째 열의 [0, N - 1] 범위의 행에 퀸을 놓은 후에,
        # c - 1번째 열까지 놓여있는 퀸들이 조건을 만족한다면
        # c + 1번째 열로 넘어가는 백트래킹 알고리즘 이용
        col[c] = r
        if check(c):
            solve(c + 1)


if __name__ == '__main__':
    N = int(input())
    answer = 0
    # col[i]: i번째 열에 있는 퀸의 행 번호
    # 예) col[2] = 5라면, 2번째 열에 퀸은 5번째 행에 위치해 있는 상태
    col = [0] * N
    solve(0)
    print(answer)
