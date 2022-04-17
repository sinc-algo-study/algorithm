"""
N x N 격자에 파이어볼 M개
위치 (r, c), 질량 m, 방향 d, 속력 s

방향은
7 0 1
6   2
5 4 3

1. 모든 파이어볼이 자신의 방향 d로 속력 s칸만큼 이동
2. 이동이 끝나고 2개 이상의 파이어볼이 있는 칸에서는
    1. 모든 파이어볼이 모두 하나로 합쳐짐
    2. 파이어볼은 4개의 파이어볼로 나누어짐
    3. ⌊(합쳐진 파이어볼 질량의 합)/5⌋     (내림임)
    4. ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋
    5. if 방향이 모두 홀수 or 모두 짝수 -> 방향은 0, 2, 4, 6
       else 방향 1, 3, 5, 7
    6. 질량이 0인 파이어볼은 소멸됨
"""
import collections
import math
from typing import List, DefaultDict, Tuple


class Fireball:
    def __init__(self, m, s, d):
        self.mass = m
        self.speed = s
        self.dir = d

    def __str__(self):
        return f"mass={self.mass}, speed={self.speed}, dir={self.dir}"


def make_fireballs_info(data: List[int]) -> DefaultDict[Tuple, List[Fireball]]:
    # 파이어볼의 위치를 key로, 파이어볼 객체를 value로 하는 dict를 만들어 반환하는 함수
    info = collections.defaultdict(list)
    for r, c, m, s, d in data:
        info[(r - 1, c - 1)].append(Fireball(m, s, d))
    return info


def move_fireballs(info: DefaultDict[Tuple, List[Fireball]]) \
        -> DefaultDict[Tuple, List[Fireball]]:
    # 모든 파이어볼을 이동시키는 함수
    new_info = collections.defaultdict(list)
    for (x, y), fireballs in info.items():
        for fireball in fireballs:
            nx, ny = x, y
            for _ in range(fireball.speed):
                nx = (nx + dx[fireball.dir] + N) % N
                ny = (ny + dy[fireball.dir] + N) % N
            new_info[(nx, ny)].append(fireball)
    return new_info


def make_divided_fireballs(fireballs: List[Fireball]) -> List[Fireball]:
    sum_mass, sum_speed, dir_mods = 0, 0, set()
    for fireball in fireballs:
        sum_mass += fireball.mass
        sum_speed += fireball.speed
        dir_mods.add(fireball.dir % 2)

    mass = math.floor(sum_mass / 5)
    if mass == 0:
        return []
    speed = math.floor(sum_speed / len(fireballs))
    dirs = [0, 2, 4, 6] if len(dir_mods) < 2 else [1, 3, 5, 7]

    divided_fireballs = []
    for i in range(4):
        divided_fireballs.append(Fireball(mass, speed, dirs[i]))
    return divided_fireballs


def merge_and_divide(info: DefaultDict[Tuple, List[Fireball]]) -> None:
    # 같은 위치에 있는 파이어볼들을 합치고 나눈 후 질량이 0이면 소멸하는 함수
    for (x, y), fireballs in info.items():
        if len(fireballs) < 2:
            # 2개 이상의 파이어볼이 있는 칸에 대해서만 합치고 나누기
            continue

        divided_fireballs = make_divided_fireballs(fireballs)
        if not divided_fireballs:
            # 질량이 0인 파이어볼은 소멸
            info[(x, y)] = []
            continue
        info[(x, y)] = divided_fireballs


def get_sum_of_mass(info: DefaultDict[Tuple, List[Fireball]]) -> int:
    # 남아 있는 파이어볼 질량의 합을 구하는 함수
    mass = 0
    for fireballs in info.values():
        for fireball in fireballs:
            mass += fireball.mass
    return mass


def solution(k, data):
    fireballs_info = make_fireballs_info(data)
    for _ in range(k):
        # 1. 모든 파이어볼 이동
        fireballs_info = move_fireballs(fireballs_info)
        # 2. 같은 위치에 있는 파이어볼들을 합치고 나눈 후 질량이 0이면 소멸
        merge_and_divide(fireballs_info)
    return get_sum_of_mass(fireballs_info)


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    # 7 0 1
    # 6   2
    # 5 4 3
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    print(solution(K, data))
