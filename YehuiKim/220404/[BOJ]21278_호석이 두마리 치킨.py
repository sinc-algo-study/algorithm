'''
1. 각 건물에서 다른 건물 사이의 거리 구하기
    => 플로이드 워셜
2. 각 조합마다 두 거리 중 짧은 쪽의 거리를 최소거리합에 더하기
3. 최소거리합, 두 건물 번호를 answer에 저장해두고 갱신하기
    => 거리가 최소 -> 작은 번호가 더 작은 쪽 -> 큰 번호가 더 작은 쪽

[[], [3], [3, 4, 5], [1, 2], [2], [2]]
0 0 0 0 0 0
0 0 2 1 3 3
0 2 0 1 1 1
0 1 1 0 2 2
0 3 1 2 0 2
0 3 1 2 2 0
'''
import sys
input = sys.stdin.readline


if "__main__"==__name__:
    n, m = map(int, input().split())
    INF = 1000000
    graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
    # 자기자신은 0으로
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==j:
                graph[i][j]=0
    # 왕복이므로 2씩 표시해줌
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b]=2
        graph[b][a]=2
    # 각 좌표를 돌되(i,j), 그 좌표를 연결하는 건물(k)로 모든 케이스를 고려하기
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
    # 치킨집 두 개를 고르기 (작은 것, 큰 것 순서가 있으므로 for 범위 아래와 같이 잡기)
    minDist, chkenMin, chkenMax = INF, 0, 0
    for i in range(1,n): # 작은 것
        for j in range(i,n+1): # 큰 것
            dist = 0
            for o in range(1,n+1):
                # 건물o에서 치킨집 i, 건물o에서 치킨집 j 사이 거리 중 최소값
                dist += min(graph[o][i], graph[o][j])
            if dist<minDist:
                minDist, chkenMin, chkenMax = dist, i, j
    print(chkenMin, chkenMax, minDist)


