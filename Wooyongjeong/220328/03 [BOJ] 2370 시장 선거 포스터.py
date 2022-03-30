import collections


def solution(n, posters):
    num = collections.defaultdict(bool)
    for l, r in posters:
        num[l] = True
        num[r] = True

    num = sorted(num.keys())

    wall = [-1] * len(num)
    for i, (l, r) in enumerate(posters):
        i1 = num.index(l)
        i2 = num.index(r)
        for j in range(i1, i2 + 1):
            wall[j] = i
    return len(set(wall))


if __name__ == '__main__':
    n = int(input())
    posters = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n, posters))
