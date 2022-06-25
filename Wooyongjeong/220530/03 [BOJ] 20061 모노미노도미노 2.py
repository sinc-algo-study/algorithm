test_case = int(input())
blue = [[0] * 6 for _ in range(4)]
green = [[0] * 4 for _ in range(6)]


def check_blue():
    global ans
    for j in range(2, 6):
        # 각 열에 블록이 몇 개 있는지 카운트
        cnt = 0
        for i in range(4):
            if blue[i][j] > 0:
                cnt += 1

        if cnt == 4:
            # 해당 열이 꽉 찼으면 제거
            remove_blue(j)
            ans += 1


def remove_blue(idx):
    for j in range(idx, 0, -1):
        for i in range(4):
            # idx열부터 1열까지 이전 열의 값을 옮겨옴
            blue[i][j] = blue[i][j - 1]
    for i in range(4):
        # 0번째 열은 0으로 초기화
        blue[i][0] = 0


def move_blue(t, x):
    y = 1
    if t == 1 or t == 2:
        # 1x1 블록 or 1x2 블록
        while True:
            # 끝에 다다르거나, 다른 블록에 부딪힐 때까지
            if y + 1 > 5 or blue[x][y + 1] != 0:
                blue[x][y] = 1
                if t == 2:
                    blue[x][y - 1] = 1
                break
            y += 1
    else:
        # 2x1 블록
        while True:
            if y + 1 > 5 or \
                    blue[x][y + 1] != 0 or blue[x + 1][y + 1] != 0:
                # 끝에 다다르거나, 다른 블록에 부딪힐 때까지
                blue[x][y], blue[x + 1][y] = 1, 1
                break
            y += 1

    check_blue()

    for i in range(4):
        for j in range(2):
            if blue[i][j] > 0:
                # 0, 1번째 열에 블록이 있으면 맨 마지막 열을 제거하고 한칸씩 땡겨지도록 함
                remove_blue(5)
                break


def check_green():
    global ans
    for i in range(2, 6):
        # 각 행에 블록이 몇 개 있는지 카운트
        cnt = 0
        for j in range(4):
            if green[i][j] > 0:
                cnt += 1

        if cnt == 4:
            # 해당 행이 꽉 찼으면 제거
            remove_green(i)
            ans += 1


def remove_green(idx):
    for i in range(idx, 0, -1):
        for j in range(4):
            # idx행부터 1행까지 이전 행의 값을 옮겨옴
            green[i][j] = green[i - 1][j]
    for j in range(4):
        # 0번째 행은 0으로 초기화
        green[0][j] = 0


def move_green(t, y):
    x = 1
    if t == 1 or t == 3:
        # 1x1 블록 or 2x1 블록
        while True:
            if x + 1 > 5 or green[x + 1][y] != 0:
                # 끝에 다다르거나, 다른 블록에 부딪힐 때까지
                green[x][y] = 1
                if t == 3:
                    green[x - 1][y] = 1
                break
            x += 1
    else:
        # 1x2 블록
        while True:
            if x + 1 > 5 or \
                    green[x + 1][y] != 0 or green[x + 1][y + 1] != 0:
                # 끝에 다다르거나, 다른 블록에 부딪힐 때까지
                green[x][y], green[x][y + 1] = 1, 1
                break
            x += 1

    check_green()

    for i in range(2):
        for j in range(4):
            if green[i][j] > 0:
                # 0, 1번째 행에 블록이 있으면 맨 마지막 열을 제거하고 한칸씩 땡겨지도록 함
                remove_green(5)
                break


"""
t = 1: 크기가 1×1인 블록을 (x, y)에 놓은 경우
t = 2: 크기가 1×2인 블록을 (x, y), (x, y+1)에 놓은 경우 -> (x, y-1), (x, y)로 생각
t = 3: 크기가 2×1인 블록을 (x, y), (x+1, y)에 놓은 경우 -> 얜 그대로
"""
ans = 0
for _ in range(test_case):
    t, x, y = map(int, input().split())
    move_blue(t, x)
    move_green(t, y)

blue_tile_cnt, green_tile_cnt = 0, 0
for i in range(4):
    for j in range(2, 6):
        if blue[i][j]:
            blue_tile_cnt += 1

for i in range(2, 6):
    for j in range(4):
        if green[i][j]:
            green_tile_cnt += 1

print(ans)
print(blue_tile_cnt + green_tile_cnt)
