rom sys import stdin
from itertools import combinations


N, K = map(int, stdin.readline().split())
words = [stdin.readline().rstrip() for _ in range(N)]

ans = 0
if K >= 5:
    arr = ['a', 'c', 'i', 'n', 't']
    can_read = set(arr)

    combi = list("bdefghjklmopqrsuvwxyz")
    ans = 0
    for candi in combinations(combi, K-5):
        cnt = 0
        for i in range(N):
            icnt = True
            word = words[i][4:-4]
            for w in word:
                if w not in can_read and w not in candi:
                    icnt = False
                    break
            if icnt:
                cnt += 1
        ans = max(ans, cnt)
print(ans)