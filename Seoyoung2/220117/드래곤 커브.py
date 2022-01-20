from sys import stdin

dxdy = (0, 1), (-1, 0), (0, -1), (1, 0)     # 우, 상, 좌, 하
N = int(stdin.readline())

# 진행 방향은 항상 같으니까 먼저 계산
# 방향 : 0->1 / 1->2 / 2->3 / 3->0
gen = [[] for _ in range(11)]
gen[0].append(0)
for i in range(1, 11):
    gen[i] = gen[i-1][:]        # 이전 세대 일단 그대로 복사
    for d in gen[i-1][::-1]:
        gen[i].append(d+1)      # 어차피 뒤에서 %4 해줄거임

check = [[False] * 101 for _ in range(101)]
for _ in range(N):
    y, x, d, gg = map(int, stdin.readline().split())
    check[x][y] = True
    for g in gen[gg]:
        x += dxdy[(g+d) % 4][0]
        y += dxdy[(g+d) % 4][1]
        check[x][y] = True

ans = 0
for i in range(100):
    for j in range(100):
        if check[i][j] and check[i+1][j] and check[i][j+1] and check[i+1][j+1]:
            ans += 1
print(ans)



