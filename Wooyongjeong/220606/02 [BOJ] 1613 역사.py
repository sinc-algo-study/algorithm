"""
플로이드-워셜을 이용하여 전후 관계를 알 수 있는지 체크
if con[before][after] => before가 after 이전에 일어났음
elif con[after][before] => before가 after 이후에 일어났음
else => 알 수 없음
"""
N, K = map(int, input().split())
con = [[False for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(K):
    before, after = map(int, input().split())
    con[before][after] = True

events = []
s = int(input())
for _ in range(s):
    before, after = map(int, input().split())
    events.append((before, after))


def floyd_warshall():
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if con[i][k] and con[k][j]:
                    con[i][j] = True


def check_history(before, after):
    if con[before][after]:
        return -1
    elif con[after][before]:
        return 1
    else:
        return 0


floyd_warshall()
for before, after in events:
    print(check_history(before, after))
