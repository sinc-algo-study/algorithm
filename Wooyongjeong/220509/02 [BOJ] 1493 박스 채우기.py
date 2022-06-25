"""
큰 큐브부터 채우는 게 유리함
-> 채우고 남은 부분 분할 정복
"""
import collections


def solution(length, width, height, cube_keys):
    global ans

    if length == 0 or width == 0 or height == 0:
        return

    k = min(length, width, height)
    cube = 0

    # 1. 현재 length, width, height의 큐브에 대해서
    # 가지고 있는 큐브 중에서 채울 수 있는 가장 큰 큐브를 선택
    for key in cube_keys:
        if key > k:
            continue
        cube = key
        break
    else:
        print(-1)
        exit(0)

    ans += 1
    cubes[cube] -= 1

    # 2. 그 큐브를 채우고 남은 애들을 분할 정복
    solution(length - cube, width, height, cube_keys)
    solution(cube, width, height - cube, cube_keys)
    solution(cube, width - cube, cube, cube_keys)


if __name__ == '__main__':
    length, width, height = map(int, input().split())
    N = int(input())
    cubes = collections.defaultdict(int)
    for _ in range(N):
        i, cnt = map(int, input().split())
        cubes[pow(2, i)] = cnt
    ans = 0
    solution(length, width, height, sorted(cubes.keys(), reverse=True))
    print(ans)
