def rotate(a):
    n = len(a)
    m = len(a[0])

    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result


def count(block):
    cnt = 0
    for b in block:
        cnt += b.count(1)
    return cnt


def solution(game_board, table):
    n = len(table)

    def find_block(x, y, arr, p):
        if x < 0 or x >= n or y < 0 or y >= n:
            return
        board = game_board if p == 0 else table
        if board[x][y] != p:
            return
        board[x][y] = 1 if p == 0 else 0
        arr.append((x, y))

        find_block(x + 1, y, arr, p)
        find_block(x, y + 1, arr, p)
        find_block(x, y - 1, arr, p)
        find_block(x - 1, y, arr, p)

    def get_trimmed_block(block):
        x_lst = [i[0] for i in block]
        y_lst = [i[1] for i in block]
        min_x, min_y = min(x_lst), min(y_lst)
        max_x, max_y = max(x_lst), max(y_lst)

        trimmed_block = []
        for x in range(min_x, max_x + 1):
            t = []
            for y in range(min_y, max_y + 1):
                t.append(1 if (x, y) in block else 0)
            trimmed_block.append(t)
        return trimmed_block

    empty_places = []
    blocks = []
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                place = []
                find_block(i, j, place, 0)
                empty_places.append(place)
            if table[i][j] == 1:
                block = []
                find_block(i, j, block, 1)
                blocks.append(block)

    trimmed = []
    for block in blocks:
        t = []
        b = get_trimmed_block(block)
        for _ in range(4):
            b = rotate(b)
            t.append(b)
        trimmed.append(t)

    answer = 0
    for place in empty_places:
        p = get_trimmed_block(place)
        for i in range(len(trimmed)):
            find = False
            for j in range(4):
                if p == trimmed[i][j]:
                    answer += count(p)
                    find = True
                    break
            if find:
                del trimmed[i]
                break

    return answer


if __name__ == '__main__':
    game_boards = [
        [[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1],
         [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]],
        [[0, 0, 0], [1, 1, 0], [1, 1, 1]]
    ]

    tables = [
        [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1],
         [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]],
        [[1, 1, 1], [1, 0, 0], [0, 0, 0]]
    ]
    for game_board, table in zip(game_boards, tables):
        print(solution(game_board, table))
