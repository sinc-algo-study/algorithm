"""
0 흰색 1 빨간색 2 파란색
"""
import collections


def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n


def reverse_direction(d):
    if d < 2:
        return (d + 1) % 2
    elif d == 2:
        return d + 1
    return d - 1


def solution(n, k, board, chess_pieces, chess_pieces_info):
    def reverse_dir_and_get_next_position(x, y, d):
        # 체스판을 벗어났거나 파란색이어서 방향을 뒤집어보고 다시 움직여 봄
        nd = reverse_direction(d)
        nx, ny = x + dx[nd], y + dy[nd]

        # 그래도 체스판을 벗어났거나 파란색이라면 움직이지 않고 종료
        if not in_range(nx, ny, n) or board[nx][ny] == 2:
            return x, y, nd
        # 갈 수 있다면 이동
        return nx, ny, nd

    def get_next_position(x, y, d):
        # 우선 말을 d 방향으로 한 칸 움직여 봄
        nx, ny = x + dx[d], y + dy[d]

        # 체스판을 벗어나는 경우나 파란색인 경우
        if not in_range(nx, ny, n) or board[nx][ny] == 2:
            # 방향을 반대로 하고 다시 이동해 봄
            return reverse_dir_and_get_next_position(x, y, d)

        # 흰색, 빨간색의 경우 거기로 이동
        if board[nx][ny] == 0 or board[nx][ny] == 1:
            return nx, ny, d

    def get_moved_pieces(piece):
        x, y, d = chess_pieces_info[piece]
        pieces = collections.deque()
        if chess_pieces[x][y]:
            idx = chess_pieces[x][y].index(piece)
        else:
            idx = 0
        m = len(chess_pieces[x][y])
        for _ in range(idx, m):
            pieces.appendleft(chess_pieces[x][y].pop())
        return pieces

    for turn in range(1, MAX_TURN + 1):
        cannot_move_pieces_cnt = 0
        for piece in range(1, k + 1):
            x, y, d = chess_pieces_info[piece]
            nx, ny, nd = get_next_position(x, y, d)

            chess_pieces_info[piece][-1] = nd

            # 말이 움직이지 않은 경우
            # 체스판 바깥 or 파란색 -> 방향 뒤집음 -> 다시 체스판 바깥 or 파란색인 경우임
            # 방향만 update
            if x == nx and y == ny:
                cannot_move_pieces_cnt += 1
                continue

            # 이동되는 체스말들을 구함
            pieces = get_moved_pieces(piece)

            # 빨간색이라면 순서를 반대로 뒤집음
            if board[nx][ny] == 1:
                pieces.reverse()

            # 이동하려는 칸으로 합침
            chess_pieces[nx][ny].extend(pieces)

            # 말이 4개 이상 쌓이면 게임 종료
            if len(chess_pieces[nx][ny]) >= 4:
                return turn

        # 모든 말이 움직일 수 없다면(=절대로 게임이 종료되지 않는 경우) 게임 종료
        if cannot_move_pieces_cnt == k:
            break

    return -1


if __name__ == '__main__':
    MAX_TURN = 1000
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    chess_pieces = [[collections.deque() for _ in range(N)] for _ in range(N)]
    chess_pieces_info = {}
    for i in range(1, K + 1):
        x, y, d = map(int, input().split())
        x, y, d = x - 1, y - 1, d - 1
        chess_pieces[x][y].append(i)
        chess_pieces_info[i] = [x, y, d]
    print(solution(N, K, board, chess_pieces, chess_pieces_info))
