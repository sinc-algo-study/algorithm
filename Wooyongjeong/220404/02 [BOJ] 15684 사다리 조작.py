def check():
    for j in range(N):
        col = j
        for row in range(H):
            if ladders[row][col] == 1:
                col += 1
            elif ladders[row][col - 1] == 1:
                col -= 1

        if col != j:
            return False
    return True


def exist_ladder(i, j):
    return (ladders[i][j] == 1) or \
           (j + 1 < N and ladders[i][j + 1] == 1) or \
           (0 <= j - 1 and ladders[i][j - 1] == 1)


def dfs(idx, cnt, max_cnt):
    global ans

    if cnt == max_cnt:
        if check():
            ans = cnt
        return

    for i in range(idx, H):
        for j in range(N - 1):
            if exist_ladder(i, j):
                continue

            ladders[i][j] = 1
            dfs(i, cnt + 1, max_cnt)
            ladders[i][j] = 0


if __name__ == '__main__':
    INF = int(1e9)
    N, M, H = map(int, input().split())
    ladders = [[0] * N for _ in range(H)]
    for _ in range(M):
        a, b = map(int, input().split())
        ladders[a - 1][b - 1] = 1

    ans = INF
    for i in range(4):
        dfs(0, 0, i)
        if ans != INF:
            break

    print(ans if ans != INF else -1)
