def dfs(me: int, graph: list[list[int]],
        visited: list[bool], dp: list[list[int]]) -> None:
    visited[me] = True
    dp[me][NOT_ADAPTOR] = 0  # 내가 얼리어답터가 아니므로 0
    dp[me][ADAPTOR] = 1  # 내가 얼리어답터이므로 1

    for friend in graph[me]:
        if visited[friend]:
            continue

        dfs(friend, graph, visited, dp)
        # 내가 얼리어답터가 아니므로 자식은 얼리어답터이어야 함
        dp[me][NOT_ADAPTOR] += dp[friend][ADAPTOR]
        # 내가 얼리어답터이므로 자식은 뭐 얼리어답터이든 아니든 상관 없음
        dp[me][ADAPTOR] += min(dp[friend][ADAPTOR], dp[friend][NOT_ADAPTOR])


def solution(graph: list[list[int]]) -> int:
    # dp[i][0]: i번째 사람이 얼리어답터가 아닐 때, 본인+아래 친구들 중 얼리어답터 최소 명수
    # dp[i][1]: i번째 사람이 얼리어답터일 때, (위와 동일)
    dp = [[0 for _ in range(2)] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    dfs(1, graph, visited, dp)
    return min(dp[1])


if __name__ == '__main__':
    N = int(input())
    NOT_ADAPTOR = 0
    ADAPTOR = 1
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    print(solution(graph))
