"""
각 단계별로 visited를 고려하는 게 뽀인트

실제로 다 바꿔보면서 ㄱㄱ
depth가 최대 10이고
자릿수도 최대 7자리라서 완전 가능
"""

import collections


def solution(n, k):
    m = len(n)
    k = int(k)

    q = collections.deque()
    visited = [[False for _ in range(k + 1)] for _ in range(MAX)]

    q.append((list(n), 0))
    visited[int(n)][0] = True

    answer = -1
    while q:
        now, cnt = q.popleft()

        if cnt == k:
            answer = max(answer, int(''.join(now)))
            continue

        for i in range(m - 1):
            for j in range(i + 1, m):
                if i == 0 and now[j] == '0':
                    continue

                now[i], now[j] = now[j], now[i]

                num = int(''.join(now))
                if not visited[num][cnt + 1]:
                    visited[num][cnt + 1] = True
                    q.append((now[:], cnt + 1))

                now[i], now[j] = now[j], now[i]

    return answer


if __name__ == '__main__':
    MAX = 1000000 + 1
    N, K = input().split()
    print(solution(N, K))
