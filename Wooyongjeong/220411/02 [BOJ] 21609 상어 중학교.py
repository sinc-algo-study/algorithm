"""
상하좌우로 연결되어 있는 애들을 블록 그룹으로 묶을 거임

그룹에는 일반 블록이 적어도 하나 있어야 되고, 그 색들은 모두 같앙 ㅑ함
검은색 블록은 포함하면 안됨. 무지개 블록은 얼마나 있든 상관 없음
그룹에 속한 블록 개수는 2 이상이어야 함

기준 블록: 무지개 블록이 아닌 블록 중 행 번호가 가장 작은 블록, 여러 개면 열 번호가 작은거

1. 크기가 가장 큰 블록 그룹을 찾음.
여러 개면 무지개 블록 수가 많은 그룹.
여러 개면 기준 블록의 행이 가장 큰 것. 여러 개면 열이 가장 큰 것
2. 1에서 찾은 블록 그룹의 모든 블록을 제거 -> B개가 제거되면 B^2 점 획득
3. 격자에 중력이 작용 (제거된 블록들 위쪽 블록들이 떨어진다는 거겠지)
    근데 검은색 블록은 중력 영향을 안받음
4. 격자가 90도 반시계 방향으로 회전
5. 다시 중력이 작용

그럼 모듈화를 해보면..
1. 블록 그룹 찾기 (계속 갱신해보면서 ㅇㅇ)
2. 블록을 제거하고 점수 획득
3. 중력 작용
4. 격자 90도 반시계로 회전
"""
import collections
import copy
import heapq


def find_max_size_block_group(board):
    """
    크기가 가장 큰 블록 그룹을 찾는 함수

    블록 개수 -> 무지개 블록 개수 ->
    기준 블록의 행이 가장 큰 것 -> 기준 블록의 열이 가장 큰 것 순으로
    """
    block_groups = []
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and not visited[i][j]:
                group, rainbow_cnt = find_block_group(i, j, board, visited)
                if not group:
                    continue
                # (블록 개수, 무지개 블록 개수, 기준 블록의 행, 기준 블록의 열)
                heapq.heappush(block_groups,
                               (-len(group), -rainbow_cnt, -i, -j, group))
    if not block_groups:
        return []
    max_size_block_group = heapq.heappop(block_groups)
    return max_size_block_group[-1]


def find_block_group(i, j, board, visited):
    """
    (i, j)부터 시작해 블록 그룹 찾는 함수
    (찾은 블록 그룹, 블록에 포함된 무지개 블록 개수) 반환
    """

    def in_range(x, y):
        # 범위를 벗어나지 않는지 확인
        return 0 <= x < N and 0 <= y < N

    color = board[i][j]
    q = collections.deque()
    group = []
    rainbow_blocks = []

    q.append((i, j))
    visited[i][j] = True
    group.append((i, j))

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny):
                continue

            if board[nx][ny] == 0 and (nx, ny) not in rainbow_blocks:
                # 무지개 블록이라면
                group.append((nx, ny))
                rainbow_blocks.append((nx, ny))
                q.append((nx, ny))
                continue

            if not visited[nx][ny] and board[nx][ny] == color:
                # 방문한 적 없는 같은 색의 블록이라면
                group.append((nx, ny))
                q.append((nx, ny))
                visited[nx][ny] = True

    if len(group) <= 1:
        return [], 0
    return group, len(rainbow_blocks)


def fall_blocks(board):
    """
    격자에 중력 작용
    """
    for j in range(N):
        for i in range(N - 1, -1, -1):
            if board[i][j] == BLANK_SPACE:
                x, y = i, j
                while x > 0 and board[x][y] == BLANK_SPACE:
                    x -= 1
                if board[x][y] == -1:
                    continue
                board[i][j], board[x][y] = board[x][y], board[i][j]


def rotate_board(board):
    """
    격자 90도 반시계 방향으로 회전
    """
    copied = copy.deepcopy(board)
    for i in range(N):
        for j in range(N):
            board[i][j] = copied[j][N - 1 - i]


def solution(board):
    score = 0

    while True:
        # 1. 크기가 가장 큰 블록 그룹을 찾는다
        block_group = find_max_size_block_group(board)
        # 블록 그룹이 존재하지 않으면 종료
        if not block_group:
            break
        # 2. 찾은 블록 그룹의 모든 블록 제거
        for (i, j) in block_group:
            board[i][j] = BLANK_SPACE
        score += len(block_group) ** 2
        # 3. 중력 작용
        fall_blocks(board)
        # 4. 90도 반시계 방향으로 회전
        rotate_board(board)
        # 5. 중력 작용
        fall_blocks(board)

    return score


if __name__ == '__main__':
    BLANK_SPACE = -2
    dxs = [-1, 0, 1, 0]
    dys = [0, -1, 0, 1]
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(solution(board))
