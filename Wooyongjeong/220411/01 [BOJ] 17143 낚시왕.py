import collections


class Shark:
    def __init__(self, s, d, z):
        self.speed = s
        self.dir = d - 1
        self.size = z


def release_sharks(sharks, board):
    shark_info = collections.defaultdict(list)
    # 상어 위치 (r, c), 속력 s, 이동 방향 d, 크기 z
    for r, c, s, d, z in sharks:
        board[r][c] = Shark(s, d, z)
        shark_info[(r, c)].append(board[r][c])
    return shark_info


def get_closest_shark(shark_info, board, j):
    for i in range(1, R + 1):
        if not shark_info[(i, j)]:
            continue
        # move_sharks()에서 상어가 같은 위치에 여러 마리 있다면
        # 크기가 가장 큰 상어만 남는 것이 보장됨
        board[i][j] = None
        return shark_info[(i, j)].pop()
    return None


def turn_shark(d):
    if 0 <= d <= 1:  # 위 <-> 아래
        return (d + 1) % 2

    if 2 <= d <= 3:  # 왼쪽 <-> 오른쪽
        return (d + 1) % 2 + 2


def move_shark(x, y, shark):
    s = shark.speed
    xx, yy = x, y
    while s > 0:
        nx = xx + dx[shark.dir]
        ny = yy + dy[shark.dir]

        if nx < 1 or R < nx or ny < 1 or C < ny:
            shark.dir = turn_shark(shark.dir)
            continue

        if 1 <= nx <= R and 1 <= ny <= C:
            xx, yy = nx, ny
            s -= 1
    return xx, yy


def move_sharks(board, shark_info):
    new_shark_info = collections.defaultdict(list)
    # 이동
    for (x, y), sharks in shark_info.items():
        if not sharks:
            continue
        shark = sharks.pop()
        board[x][y] = None
        nx, ny = move_shark(x, y, shark)
        new_shark_info[(nx, ny)].append(shark)
    return new_shark_info


def cannibalism(board, shark_info):
    # 한 칸에 여러 마리 상어가 있는지 검사, 그렇다면 크기가 가장 큰 상어 빼고 다 제거
    for (x, y), sharks in shark_info.items():
        if len(sharks) < 2:
            continue
        sharks.sort(key=lambda s: s.size, reverse=True)
        del shark_info[(x, y)][1:]

    # board, shark_info에 반영
    for (x, y), sharks in shark_info.items():
        board[x][y] = sharks[0]


def solution(sharks):
    board = [[None] * (C + 1) for _ in range(R + 1)]
    shark_info = release_sharks(sharks, board)
    ans = 0
    # 낚시왕이 가장 오른쪽 열의 오른쪽 칸에 이동하면 멈춤
    # 1. 낚시왕이 오른쪽으로 한 칸 이동한다
    for j in range(1, C + 1):
        # 2. 땅과 제일 가까운 상어를 잡는다
        shark = get_closest_shark(shark_info, board, j)
        if shark is not None:
            ans += shark.size
        # 3. 상어가 이동한다
        shark_info = move_sharks(board, shark_info)
        # 여러 마리의 상어가 한 칸에 있다면, 가장 크기가 큰 상어가 나머지 상어를 잡아먹음
        cannibalism(board, shark_info)
    return ans


if __name__ == '__main__':
    dx = [-1, 1, 0, 0]  # 위, 아래, 오른쪽, 왼쪽
    dy = [0, 0, 1, -1]
    R, C, M = map(int, input().split())
    sharks = [list(map(int, input().split())) for _ in range(M)]
    print(solution(sharks))
