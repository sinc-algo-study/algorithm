"""
트리 + DP
"""
import sys
sys.setrecursionlimit(10**6)


def solution(n, populations, graph):
    def go(curr):
        visited[curr] = True
        dp[curr][0] = 0
        dp[curr][1] = populations[curr]

        for node in graph[curr]:
            if not visited[node]:
                go(node)
                dp[curr][0] += max(dp[node])
                dp[curr][1] += dp[node][0]

    visited = [False] * (n + 1)
    # dp[i][0]: i번째 마을을 우수 마을로 선정하지 않았을 경우의 인구수 총합의 최댓값
    # -> 자식 노드가 우수 마을인지 여부는 상관 없음
    # dp[i][1]: i번째 마을을 우수 마을로 선정하였을 경우의 인구수 총합의 최댓값
    # -> 자식 노드는 무조건 우수 마을이어야함
    dp = [[0] * 2 for _ in range(n + 1)]
    go(1)
    return max(dp[1])


if __name__ == '__main__':
    N = int(input())
    populations = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    print(solution(N, populations, graph))
