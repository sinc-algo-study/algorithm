import collections


def dfs(cur):
    cnt = 0

    for child in children[cur]:
        cnt += dfs(child)

    if animals[cur] == 'W':
        return max(cnt - animals_counts[cur], 0)

    return cnt + animals_counts[cur]


if __name__ == '__main__':
    N = int(input())
    animals = collections.defaultdict(int)
    animals_counts = collections.defaultdict(int)

    children = [[] for _ in range(N + 1)]
    for node in range(2, N + 1):
        animal, cnt, parent = input().split()
        cnt, parent = int(cnt), int(parent)

        animals[node] = animal
        animals_counts[node] = cnt
        children[parent].append(node)
    print(dfs(1))
