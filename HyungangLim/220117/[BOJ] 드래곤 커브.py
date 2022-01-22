'''

1. 주어진 커브를 그린다.
2. 모든 좌표를 1*1 사각형의 시작점으로 잡고 검사한다.

(0 ≤ x, y ≤ 100, 0 ≤ d ≤ 3, 0 ≤ g ≤ 10)
-> [0][0] ~ [100][100] 나와야 하므로 총 [101][101] 필요
-> g <= 10 이니까..

※ 입력 주의 !!! 행열이 아닌 x,y 좌표로 주어진다!! r,c가 아닌 c,r로 받아야 함
x, y, d, g -> 행, 열, 시작방향, 세대
d : 0, 1, 2, 3 -> 우, 상, 좌, 하


시계방향으로 돌린 것을 복제해서 이어붙일떄?
-> 기존 방향의 역을 +1 씩 해서 이동하면 된다

ex)
    우 : 0
    우+상 : 0 + 1
    우상+좌상 : 0 1 + 2 1
    우상좌상+좌하좌상 : 0 1 2 1 + 2 3 2 1

'''


def find_square(r, c):
    check_dir = [0, 3, 2, 1]  # 우 하 좌 상  순으로 검사 실시
    for i in check_dir:
        r += r_list[i]
        c += c_list[i]
        if board[r][c] == 0:
            return False
    return True


def make_curv():
    for curv in curvs:  # 각 커브를 격자에 그대로 그린다
        c, r, d, g = curv

        # 세대에 맞춰서 각 커브마다 경로를 만들고 그 경로를 따라 점을 찍는다
        path = [d]  # 일단 0세대 방향은 가지고 있어야 함

        for _ in range(g):
            temp = [(n + 1) % 4 for n in reversed(path)]
            path += temp

        # 미리 구한 커브의 경로에 따라 점을 찍는다
        board[r][c] = 1
        for p in path:
            r += r_list[p]
            c += c_list[p]
            board[r][c] = 1


if __name__ == '__main__':
    answer = 0

    N = int(input())
    curvs = [list(map(int, input().split())) for _ in range(N)]
    board = [[0 for _ in range(101)] for _ in range(101)]

    # d : 0, 1, 2, 3 -> 우, 상, 좌, 하
    r_list = [0, -1, 0, 1]
    c_list = [1, 0, -1, 0]

    make_curv()
    for i in range(100):  # square 검사는 [99][99] 까지만 해야 한다
        for j in range(100):
            if find_square(i, j):
                answer += 1

    print(answer)
