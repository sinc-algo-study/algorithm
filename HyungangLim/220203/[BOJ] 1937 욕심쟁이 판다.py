'''

주의 : 가장 많이 먹을 수 있는 대나무의 양이 아니라 가장 긴 이동 경로이다.

브루트포스로 짠다면?

->

모든 좌표를 시작점으로 DFS ??
500 * 500 너무 길다. DP로 시간을 줄인다.

->

dp[i][j] 을 뭘로 잡을 것인가?

->
1. [i][j]까지 가장 많이 밟으며 오는 수
2. [i][j]에서 가장 많이 밟으며 나아갈 수 있는 수
둘 중 뭐지..?

->

굳이 이미 했던 걸 또 안 해도 된다. 가 DP의 핵심...
그럼 그 "이미 했던 거"의 결과를 저장 해놓는 게 dp일 것이고..
"이미 했던 거"는 "여기서 얼마나 더 나아갈 수 있을 것이냐"일 것

->

check[][]의 필요 여부?
dp[nr][nc] 구하다가 dp[r][c]를 마주쳤을때를 어떻게 고려할 것인가?

->

나보다 큰 곳으로만 이동 가능하기 때문에 이미 지나온 길에 다시 갈 일은 없다
나보다 작으면 이미 방문을 했건 안 했건 간에 상관 없이 이동하지 못한다
즉, 고려할 필요 없다!

->
나보다 board[i][j]값이 작은 점을 고려할 필요 없다.
즉, dp[i][j]는 [i][j]를 "시작점"으로 하여 가장 멀리 갈 수 있는 경로


'''


import sys
sys.setrecursionlimit(25000)


def dfs(r, c):
    dp[r][c] = 0
    for d in range(4):
        nr = r + r_list[d]
        nc = c + c_list[d]
        if not (-1 < nr < N and -1 < nc < N and board[nr][nc] > board[r][c]):
            continue
        if dp[nr][nc] == -1:
            dfs(nr, nc)
        dp[r][c] = max(dp[r][c], dp[nr][nc])
    dp[r][c] += 1


def solution():
    ans = 0
    for i in range(N):
        for j in range(N):
            if dp[i][j] == -1:
                dfs(i, j)
            ans = max(ans, dp[i][j])
    return ans


if __name__ == '__main__':
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dp = [[-1 for _ in range(N)] for _ in range(N)]
    r_list = [-1, 1, 0, 0]
    c_list = [0, 0, -1, 1]
    print(solution())