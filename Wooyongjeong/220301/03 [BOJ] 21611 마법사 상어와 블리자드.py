import collections


def solution(n, m, board, blizzards):
    def make_beads_info():
        info = {}
        dir_x = [0, 1, 0, -1]
        dir_y = [-1, 0, 1, 0]
        x = n // 2
        y = n // 2
        cnt = 1
        d = 0
        number = 1

        while True:
            for i in range(2):
                for j in range(cnt):
                    x += dir_x[d]
                    y += dir_y[d]

                    info[number] = [x, y]
                    number += 1
                    if x == 0 and y == 0:
                        return info
                d = (d + 1) % 4
            cnt += 1

    def cast_blizzard(blizzard):
        x = n // 2
        y = n // 2

        d, s = blizzard
        for i in range(s):
            x += dx[d]
            y += dy[d]
            board[x][y] = 0

    def move_beads():
        is_move = False
        q = collections.deque()
        for i in range(1, n * n):
            x, y = beads_info[i]
            if board[x][y] != 0:
                q.append(board[x][y])
                continue
            if not is_move and i + 1 < n * n:
                nx, ny = beads_info[i + 1]
                if board[nx][ny] != 0:
                    is_move = True

        if not is_move:
            return False

        for i in range(1, n * n):
            x, y = beads_info[i]
            if not q:
                board[x][y] = 0
                continue
            board[x][y] = q.popleft()

        return True

    def explode_beads():
        explode_cnt = 0
        for i in range(1, n * n):
            x, y = beads_info[i]
            if board[x][y] == 0:
                continue
            q = collections.deque()
            q.append(i)
            for j in range(i + 1, n * n):
                nx, ny = beads_info[j]
                if board[x][y] != board[nx][ny]:
                    break
                q.append(j)

            if len(q) < 4:
                continue
            explode_cnt += board[x][y] * len(q)
            while q:
                x, y = beads_info[q.popleft()]
                board[x][y] = 0

        return explode_cnt

    def transform_beads():
        q = collections.deque()
        for i in range(1, n * n):
            x, y = beads_info[i]
            if board[x][y] == 0:
                continue

            cnt = 1
            for j in range(i + 1, n * n):
                nx, ny = beads_info[j]
                if board[x][y] != board[nx][ny]:
                    break
                cnt += 1
                board[nx][ny] = 0

            q.append(cnt)
            q.append(board[x][y])
            board[x][y] = 0

        for i in range(1, n * n):
            x, y = beads_info[i]
            if not q:
                board[x][y] = 0
                continue
            board[x][y] = q.popleft()

    answer = 0
    beads_info = make_beads_info()
    for blizzard in blizzards:
        cast_blizzard(blizzard)
        move_beads()
        answer += explode_beads()
        while True:
            is_move = move_beads()
            if not is_move:
                break
            answer += explode_beads()
        transform_beads()
    return answer


if __name__ == '__main__':
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    blizzards = [list(map(int, input().split())) for _ in range(M)]
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    print(solution(N, M, board, blizzards))
