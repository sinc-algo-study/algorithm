import collections


def get_next_locations(location, board):
    next_locations = []
    location = list(location)
    x1, y1 = location[0]
    x2, y2 = location[1]
    # 회전하지 않고 상하좌우로 이동
    for i in range(4):
        nx1 = x1 + dx[i]
        ny1 = y1 + dy[i]
        nx2 = x2 + dx[i]
        ny2 = y2 + dy[i]
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            # 두 칸이 모두 비어있다면
            next_locations.append({(nx1, ny1), (nx2, ny2)})

    # 회전하며 이동
    if x1 == x2:
        # 가로로 놓여 있던 경우
        if board[x1 - 1][y1] == 0 and board[x2 - 1][y2] == 0:
            # 위로 회전이 가능한 경우
            next_locations.append({(x1, y1), (x1 - 1, y1)})  # 왼쪽 위로 회전
            next_locations.append({(x2, y2), (x2 - 1, y2)})  # 오른쪽 위로 회전
        if board[x1 + 1][y1] == 0 and board[x2 + 1][y2] == 0:
            # 아래로 회전이 가능한 경우
            next_locations.append({(x1, y1), (x1 + 1, y1)})  # 오른쪽 아래로 회전
            next_locations.append({(x2, y2), (x2 + 1, y2)})  # 왼쪽 아래로 회전
    elif y1 == y2:
        # 세로로 놓여 있던 경우
        if board[x1][y1 - 1] == 0 and board[x2][y2 - 1] == 0:
            # 왼쪽으로 회전이 가능한 경우
            next_locations.append({(x1, y1), (x1, y1 - 1)})  # 왼쪽 위로 회전
            next_locations.append({(x2, y2), (x2, y2 - 1)})  # 왼쪽 아래로 회전
        if board[x1][y1 + 1] == 0 and board[x2][y2 + 1] == 0:
            # 오른쪽으로 회전이 가능한 경우
            next_locations.append({(x1, y1), (x1, y1 + 1)})  # 오른쪽 위로 회전
            next_locations.append({(x2, y2), (x2, y2 + 1)})  # 오른쪽 아래로 회전
    return next_locations


def solution(board):
    n = len(board)
    # board의 가장자리를 1로 채운 new_board
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    location = {(1, 1), (1, 2)}
    q = collections.deque()
    q.append((location, 0))  # (현재 위치, 시간)
    visited = [location]

    while q:
        loc, cost = q.popleft()
        if (n, n) in loc:
            return cost
        for next_location in get_next_locations(loc, new_board):
            if next_location not in visited:
                q.append((next_location, cost + 1))
                visited.append(next_location)
    return 0


if __name__ == '__main__':
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1],
             [0, 0, 0, 0, 0]]
    print(solution(board))
