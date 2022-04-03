from sys import stdin

N, M, x, y, K = map(int, stdin.readline().split())
nums = [list(map(int, stdin.readline().split())) for _ in range(N)]
order = list(map(int, stdin.readline().split()))

dice = [0] * 6
'''
  2
4 1 3
  5
  0
  
1 : dice 0=4, 1=3, 2=2, 3=0, 4=1, 5=5
2 : dice 0=3, 1=4, 2=2, 3=1, 4=0, 5=5
3 : dice 0=5, 1=2, 2=0, 3=3, 4=4, 5=1
4 : dice 0=2, 1=5, 2=1, 3=3, 4=4, 5=0
'''
for o in order:
    # 주사위 이동
    if o == 1 and y+1 < M:
        y += 1
        dice[0], dice[1], dice[3], dice[4] = dice[4], dice[3], dice[0], dice[1]
    elif o == 2 and y-1 >= 0:
        y -= 1
        dice[0], dice[1], dice[3], dice[4] = dice[3], dice[4], dice[1], dice[0]
    elif o == 3 and x-1 >= 0:
        x -= 1
        dice[0], dice[1], dice[2], dice[5] = dice[5], dice[2], dice[0], dice[1]
    elif o == 4 and x+1 < N:
        x += 1
        dice[0], dice[1], dice[2], dice[5] = dice[2], dice[5], dice[1], dice[0]
    else:
        continue
    # 값 복사
    if nums[x][y] == 0:
        nums[x][y] = dice[1]
    else:
        dice[1] = nums[x][y]
        nums[x][y] = 0
    print(dice[0])
