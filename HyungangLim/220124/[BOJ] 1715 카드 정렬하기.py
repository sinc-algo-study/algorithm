'''

min heap 이용
최소 묶음 두개 뽑아서 비교 후 넣기 반복

4180ms... 이게 맞아?

'''

import heapq


def solution():
    ans = 0
    while len(cards) != 1:
        first = heapq.heappop(cards)
        second = heapq.heappop(cards)
        heapq.heappush(cards, first + second)
        ans += first + second
    return ans


if __name__ == '__main__':
    N = int(input())
    cards = []
    for _ in range(N):
        heapq.heappush(cards, int(input()))
    print(solution())
