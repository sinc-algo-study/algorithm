import collections


def bfs(x, y, field, visited):
    cnt = 1  # 터지는 뿌요들의 개수
    q = collections.deque()
    q.append((x, y))
    puyo = [(x, y)]  # 터져야 하는 뿌요들 list
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M \
                    and not visited[nx][ny] and field[x][y] == field[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                puyo.append((nx, ny))
                cnt += 1

    return cnt, puyo


def puyo_puyo(puyo, field):
    # 1. 뿌요들을 터뜨림
    for x, y in puyo:
        field[x][y] = '.'
    # 2. 뿌요들을 아래로 떨어뜨림
    for i in range(N - 1, -1, -1):
        for j in range(M - 1, -1, -1):
            if field[i][j] == '.':
                for k in range(i - 1, -1, -1):
                    if field[k][j] != '.':
                        field[k][j], field[i][j] = field[i][j], field[k][j]
                        break


def solution(field):
    combo = 0
    while True:
        puyo_cnt = 0
        puyo = []
        visited = [[False] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if field[i][j] == '.' or visited[i][j]:
                    continue
                cnt, p = bfs(i, j, field, visited)
                if cnt >= 4:  # 같은 색의 뿌요들이 4개 이상 모여있어야 터짐
                    puyo_cnt += cnt
                    puyo.extend(p)
        if puyo_cnt == 0:
            return combo

        combo += 1
        puyo_puyo(puyo, field)


if __name__ == '__main__':
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    N = 12
    M = 6
    field = [list(input()) for _ in range(N)]
    print(solution(field))
