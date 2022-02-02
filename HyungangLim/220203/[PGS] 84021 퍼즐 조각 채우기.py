'''

넣는 방식에 따라서 최대 개수가 달라질 일은 없다.
즉, 그냥 맞는 구멍을 찾을 때마다 넣기만 하면 된다.

'''

from collections import deque
from collections import defaultdict


global N, check, pairs
r_list = [-1, 1, 0, 0]
c_list = [0, 0, -1, 1]


def rotate_table(table):
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[j][N - i - 1] = table[i][j]
    return result


def puzzle_to_string(board):

    # [0][0] ~ [49][49]
    min_r, min_c, max_r, max_c = 50, 50, -1, -1
    for pair in pairs:
        r, c = pair[0], pair[1]
        min_r, min_c = min(min_r, r), min(min_c, c)
        max_r, max_c = max(max_r, r), max(max_c, c)

    puzzle_str = []
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            puzzle_str.append('0' if board[r][c] == 0 else '1')
        puzzle_str.append('n')

    return ''.join(puzzle_str)


def bfs(r, c, board):  # return puzzle_string
    global pairs

    que = deque()
    pairs = []  # 퍼즐을 나타내는 좌표들을 가진다
    check[r][c] = True
    que.append((r, c))
    pairs.append((r, c))

    size = 1
    while que:
        pair = que.popleft()
        for d in range(4):
            nr = pair[0] + r_list[d]
            nc = pair[1] + c_list[d]

            if not (-1 < nr < N and -1 < nc < N):
                continue
            if check[nr][nc] or board[nr][nc] == 0:
                continue
            check[nr][nc] = True
            que.append((nr, nc))
            pairs.append((nr, nc))
            size += 1

    return puzzle_to_string(board), size


def solution(game_board, table):
    global N, check
    N = len(game_board)
    check = [[False] * N for _ in range(N)]

    # 일단 game_board 를 수정한다 0 -> 1
    # bfs 하나로 game_board, table 모두 처리하기 위함
    for i in range(N):
        for j in range(N):
            game_board[i][j] = 0 if game_board[i][j] == 1 else 1

    # game_board 에서 퍼즐 조각 추출
    puzzle_dict = defaultdict(int)  # key : vale == puzzle_string : cnt
    for i in range(N):
        for j in range(N):
            if (not check[i][j]) and game_board[i][j] == 1:
                # size는 여기선 사용하지 않음
                puzzle_string, size = bfs(i, j, game_board)
                puzzle_dict[puzzle_string] += 1

    # talbe 4번 회전 돌리면서 딱 들어맞는 퍼즐조각 찾는다
    answer = 0
    for _ in range(4):
        table = rotate_table(table)
        check = [[False] * N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if check[i][j] or table[i][j] == 0:
                    continue

                puzzle_string, size = bfs(i, j, table)

                if puzzle_string in puzzle_dict:
                    puzzle_dict[puzzle_string] -= 1
                    answer += size

                    if puzzle_dict[puzzle_string] == 0:
                        puzzle_dict.pop(puzzle_string)
                    for (r, c) in pairs:
                        table[r][c] = 0

    return answer


if __name__ == '__main__':
    game_board = [[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1],
                  [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]]
    table = [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1],
             [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]

    print(solution(game_board, table))
