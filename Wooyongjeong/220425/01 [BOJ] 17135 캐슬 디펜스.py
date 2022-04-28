"""
성에 궁수 3명을 놓아보는 최대 경우의 수는 15C3 = 455개

castle_defense()에서
1. 서순을 잘 짜자 (궁수의 사정거리에서 벗어났음에도 candidates에 넣고 있었음)
2. candidates 중에서 궁수가 공격할 적을 선택할 때
    - 사정거리도 고려했어야 됐는데 빼먹고 가장 왼쪽만 고려했었음,,
    - 사정거리가 되면 모두 candidates에 넣기 때문에 가장 가까운 적을 고려하지 못했음!
"""
import collections
import copy
from itertools import combinations


def castle_defense(archers: tuple, enemies: dict[tuple, bool]) -> int:
    kill_cnt: int = 0

    while enemies:
        # 궁수들이 공격할 적을 선택
        died = set()
        for archer in archers:
            enemy = find_enemy(archer, enemies)
            if enemy == CANNOT_ATTACK:
                continue
            died.add(enemy)

        # 선택된 적들을 죽임
        for enemy in died:
            del enemies[enemy]
            kill_cnt += 1

        # 적들이 이동
        enemies = move_enemies(enemies)

    return kill_cnt


def find_enemy(archer: int, enemies: dict[tuple, bool]) -> tuple[int, int]:
    q = collections.deque()
    visited = set()
    q.append((N - 1, archer, 1))  # (x, y, d)
    visited.add((N - 1, archer))

    candidates = []
    while q:
        x, y, d = q.popleft()

        if d > D:  # 궁수의 사정거리를 벗어나면 종료
            break

        if (x, y) in enemies:  # 공격할 수 있는 적 발견
            candidates.append((x, y, d))
            continue

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny) or (nx, ny) in visited:
                continue
            q.append((nx, ny, d + 1))
            visited.add((nx, ny))

    # 가장 가깝고, 가장 왼쪽에 있는 적을 선택하기 위함
    candidates.sort(key=lambda enemy: (enemy[2], enemy[1]))
    if not candidates:
        return CANNOT_ATTACK
    return candidates[0][:2]


def in_range(x: int, y: int) -> bool:
    return 0 <= x < N and 0 <= y < M


def move_enemies(enemies: dict[tuple, bool]) -> dict[tuple, bool]:
    new_enemies = {}
    for (x, y) in enemies:
        if x == N - 1:  # 성이 있는 칸으로 이동한 경우
            continue
        new_enemies[(x + 1, y)] = True
    return new_enemies


def solution(enemies: dict[tuple, bool]) -> int:
    answer: int = 0
    for archers in combinations(range(M), ARCHER_SIZE):
        copied_enemies = copy.deepcopy(enemies)
        answer = max(answer, castle_defense(archers, copied_enemies))
    return answer


if __name__ == '__main__':
    ARCHER_SIZE = 3
    CANNOT_ATTACK = (-1, -1)
    dxs = [0, -1, 0]  # ←, ↑, →
    dys = [-1, 0, 1]
    N, M, D = map(int, input().split())
    enemies = {}
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(M):
            if tmp[j] == 1:
                enemies[(i, j)] = True
    print(solution(enemies))
