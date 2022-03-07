"""
1. 동전은 무조건 2개
2. 상하좌우 버튼을 눌러보며 동전을 떨어뜨려봄. (btn_click_cnt를 증가시켜 가며)
    * 동전 떨어졌는지 확인 후 동전이 몇 개 떨어졌는지 체크
        - 동전이 1개 떨어졌으면, answer 갱신 후 종료
        - 동전이 2개 떨어졌으면, 무시하고 다른 방향 버튼 눌러봄 (continue)
        - 동전이 안 떨어졌다면, 현재 동전 위치를 갱신하여 다시 버튼 눌러봄
            coins = [(nx1, ny1), (nx2, ny2)] 로 갱신한 이후
            dfs(coins, btn_click_cnt + 1) 호출
    * 단, btn_click_cnt가 10 이상이거나 answer보다 크다면 종료
"""


def is_fallen(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return True
    return False


def dfs(coins, btn_click_cnt):
    global answer

    if btn_click_cnt >= 10 or btn_click_cnt >= answer:
        return

    x1, y1 = coins[0]
    x2, y2 = coins[1]
    for d in range(4):
        nx1 = x1 + dx[d]
        ny1 = y1 + dy[d]
        nx2 = x2 + dx[d]
        ny2 = y2 + dy[d]

        coin_fall_cnt = 0
        if is_fallen(nx1, ny1):
            coin_fall_cnt += 1
        if is_fallen(nx2, ny2):
            coin_fall_cnt += 1

        # 동전 2개가 모두 떨어짐
        if coin_fall_cnt == 2:
            continue
        # 동전 1개만 떨어짐 (정답)
        elif coin_fall_cnt == 1:
            # 버튼을 누른 상태이므로 btn_click_cnt + 1과 비교 해야함
            answer = min(answer, btn_click_cnt + 1)
            return
        # 동전이 안 떨어짐
        if board[nx1][ny1] == '#':
            nx1, ny1 = x1, y1
        if board[nx2][ny2] == '#':
            nx2, ny2 = x2, y2

        new_coins = [(nx1, ny1), (nx2, ny2)]
        dfs(new_coins, btn_click_cnt + 1)


if __name__ == '__main__':
    INF = int(1e9)
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    N, M = map(int, input().split())
    # 'o': 동전, '.': 빈 칸, '#' : 벽
    board = [list(input()) for _ in range(N)]

    answer = INF
    coins = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'o':
                coins.append((i, j))
    dfs(coins, 0)
    print(answer if answer != INF else -1)
