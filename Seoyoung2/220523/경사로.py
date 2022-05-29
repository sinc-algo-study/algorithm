from sys import stdin

N, L = map(int, stdin.readline().split())
grid = [[-1] * N for _ in range(N)]
rgrid = [[-1] * N for _ in range(N)]
for i in range(N):
    nums = list(map(int, stdin.readline().split()))
    for j in range(N):
        grid[i][j] = nums[j]
        rgrid[j][i] = nums[j]


def check_road(arr):
    prev = arr[0]
    j = cnt = 0
    while j < N:
        if arr[j] == prev:
            cnt += 1
            j += 1
        elif arr[j] == prev+1:
            if cnt < L:     # 경사로 놓을 자리 없음
                return False
            cnt = 1
            prev += 1
            j += 1
        elif arr[j] == prev-1:
            for l in range(L):
                if j+l >= N:  # 배열 범위 초과
                    return False
                if arr[j] != arr[j+l]:    # 같은 높이 아니어서 불가능
                    return False
            cnt = 0
            prev -= 1
            j += L
        else:   # 경사 차이가 2 이상
            return False
    return True


ans = 0
for i in range(N):
    if check_road(grid[i]):
        ans += 1
    if check_road(rgrid[i]):
        ans += 1
print(ans)