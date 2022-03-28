from sys import stdin

'''
가장 처음에 양분은 모든 칸에 5만큼 들어있다.
- 봄 : 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가 (나이가 어린 나무부터)
    만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
- 여름 : 봄에 죽은 나무가 양분으로 변하게 된다. 
    각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 소수점 아래는 버린다.
- 가을 : 나무가 번식한다. 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다. 
    상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
- 겨울 : S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다. 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.
'''
N, M, K = map(int, stdin.readline().split())
A = [list(map(int, stdin.readline().split())) for _ in range(N)]

food = [[5] * N for _ in range(N)]
age = [[[] for _ in range(N)] for _ in range(N)]    # 칸에 여러 개의 나무가 심어져 있을 수도 있음
for _ in range(M):
    x, y, z = map(int, stdin.readline().split())
    age[x-1][y-1].append(z)  # 나무의 위치, 나무의 나이
while K > 0:
    die = []
    # spring
    for i in range(N):
        for j in range(N):
            if age[i][j]:
                age[i][j].sort()
                for _ in range(len(age[i][j])):
                    num = age[i][j].pop(0)
                    if num <= food[i][j]:
                        food[i][j] -= num
                        age[i][j].append(num+1)
                    else:
                        die.append((i, j, num))
    # summer
    while die:
        x, y, z = die.pop()
        food[x][y] += z // 2
    # fall
    for i in range(N):
        for j in range(N):
            for ab in age[i][j]:
                if ab % 5 == 0:
                    for dx, dy in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            age[nx][ny].append(1)
    # winter
    for i in range(N):
        for j in range(N):
            food[i][j] += A[i][j]
    K -= 1

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(age[i][j])
print(ans)

