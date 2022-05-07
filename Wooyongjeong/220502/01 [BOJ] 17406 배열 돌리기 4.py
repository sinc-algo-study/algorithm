import collections
import copy
import itertools


def in_range(x: int, y: int, min_x: int, min_y: int,
             max_x: int, max_y: int) -> bool:
    return min_x <= x <= max_x and min_y <= y <= max_y


def rotate(r: int, c: int, s: int, a: list[list[int]]) -> None:
    # 중앙부터 시작해 한 칸씩 왼쪽 위로 이동하여 해당 border를 회전시킴
    for i in range(1, s + 1):
        max_x, max_y = r + i, c + i
        min_x, min_y = r - i, c - i

        tmp = a[min_x][min_y]
        q = collections.deque()
        q.append((min_x, min_y + 1, 0))

        while True:
            x, y, d = q.popleft()
            a[x][y], tmp = tmp, a[x][y]  # swap

            if x == min_x and y == min_y:
                break

            nx, ny = x + dx[d], y + dy[d]
            if not in_range(nx, ny, min_x, min_y, max_x, max_y):
                d += 1
                nx, ny = x + dx[d], y + dy[d]
            q.append((nx, ny, d))


def get_array_value(a: list[list[int]]) -> int:
    # 배열 a의 각 행에 있는 모든 수의 합 중 최솟값을 찾아 반환하는 함수
    array_value = INF
    for i in range(N):
        array_value = min(array_value, sum(a[i]))
    return array_value


def solution(a: list[list[int]], rotate_infos: list[list[int]]) -> int:
    ans = INF
    # 브루트포스로 회전 연산의 순서를 모두 다 바꿔서 회전시켜봄
    for candidates in itertools.permutations(rotate_infos):
        copied = copy.deepcopy(a)
        for r, c, s in candidates:
            rotate(r - 1, c - 1, s, copied)
        ans = min(ans, get_array_value(copied))
    return ans


if __name__ == '__main__':
    INF = int(1e9)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    N, M, K = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(N)]
    rotate_infos = [list(map(int, input().split())) for _ in range(K)]
    print(solution(a, rotate_infos))
