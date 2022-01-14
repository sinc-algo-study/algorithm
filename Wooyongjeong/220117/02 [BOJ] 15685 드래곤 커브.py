def get_next_generation_dirs(dirs):
    # dirs를 회전시켜 다음 세대의 dirs를 반환
    rotated_dirs = []
    for d in dirs:
        rotated_dirs.append((d + 1) % 4)
    return rotated_dirs


def make_curve_dirs(d, g):
    # g세대까지 방향 d부터 시작하는 dirs 반환
    dirs = [d]  # 0세대
    for _ in range(g):  # 1세대 ~ g세대
        dirs += get_next_generation_dirs(dirs[::-1])
    return dirs


def solution(curves):
    # 0 <= x <= 100, 0 <= y <= 100
    board = [[0 for _ in range(MAX + 1)] for _ in range(MAX + 1)]

    # 각 curve마다 curve_dirs를 이용하여 board에 표시
    for curve in curves:
        # 이번 문제에서 입력으로 주어지는 x, y는 x가 가로, y가 세로
        # 평소 2차원 배열 풀던 행열과 다르게 봐야 함
        y, x, d, g = curve
        board[x][y] = 1
        curve_dirs = make_curve_dirs(d, g)

        for curve_dir in curve_dirs:
            x += dx[curve_dir]
            y += dy[curve_dir]
            # 문제 조건: board를 벗어나는 드래곤 커브는 없음
            board[x][y] = 1

    answer = 0
    for i in range(MAX):
        for j in range(MAX):
            if board[i][j] != 0 and board[i + 1][j] != 0 and \
                    board[i][j + 1] != 0 and board[i + 1][j + 1] != 0:
                answer += 1
    return answer


if __name__ == '__main__':
    MAX = 100
    N = int(input())
    # (시작 x좌표) x, (시작 y좌표) y, (시작 방향) d, (세대) g
    dragon_curves = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, -1, 0, 1]  # 0 →, 1 ↑, 2 ←, 3 ↓
    dy = [1, 0, -1, 0]
    print(solution(dragon_curves))
