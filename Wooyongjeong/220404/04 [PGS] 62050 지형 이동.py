import collections


def bfs(x, y, number, n, height, land, groups):
    """
    사다리 없이 이동 가능한 부분들을 하나의 노드(number로 groups에 표시)로 묶는 함수
    """
    def possible(nx, ny):
        if 0 <= nx < n and 0 <= ny < n and \
                groups[nx][ny] == 0 and \
                abs(land[nx][ny] - land[x][y]) <= height:
            return True
        return False

    q = collections.deque()
    q.append((x, y))
    groups[x][y] = number

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not possible(nx, ny):
                continue
            q.append((nx, ny))
            groups[nx][ny] = number


def get_groups_weights(n, land, groups):
    """
    노드간에 이동 가능한 간선 중 가중치가 최소인 간선을 찾는 함수
    """
    def possible(x, y, nx, ny):
        if 0 <= nx < n and 0 <= ny < n and groups[x][y] != groups[nx][ny]:
            return True
        return False

    # weights[(from_group, to_group)] = weight
    # from_group에서 to_group으로 갈 때에 최소 높이의 사다리 높이 weight
    weights = collections.defaultdict(lambda: int(1e9))

    for i in range(n):
        for j in range(n):
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if not possible(i, j, nx, ny):
                    continue
                from_group = groups[i][j]
                to_group = groups[nx][ny]
                dist = abs(land[nx][ny] - land[i][j])

                weights[(from_group, to_group)] = \
                    min(weights[(from_group, to_group)], dist)

    return weights


def find_parent(parents, x):
    if x != parents[x]:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]


def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def get_ladder_cost(weights, group_number):
    """
    Minimum Spanning Tree를 이용하여 사다리 설치 비용의 최솟값을 찾는 함수
    """
    weights = sorted(weights.items(), key=lambda x: x[1])
    cost = 0
    parents = [i for i in range(group_number)]

    for (from_group, to_group), dist in weights:
        if find_parent(parents, from_group) != find_parent(parents, to_group):
            union_parent(parents, from_group, to_group)
            cost += dist

    return cost


def solution(land, height):
    n = len(land)
    groups = [[0] * n for _ in range(n)]

    group_number = 1
    for i in range(n):
        for j in range(n):
            if groups[i][j] == 0:
                bfs(i, j, group_number, n, height, land, groups)
                group_number += 1

    weights = get_groups_weights(n, land, groups)
    return get_ladder_cost(weights, group_number)


if __name__ == '__main__':
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    lands = [
        [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]],
        [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
    ]
    heights = [3, 1]
    for land, height in zip(lands, heights):
        print(solution(land, height))
