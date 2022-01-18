import heapq


if __name__ == '__main__':
    N = int(input())
    cards = []
    for _ in range(N):
        heapq.heappush(cards, int(input()))

    answer = 0
    while len(cards) != 1:
        sum_value = heapq.heappop(cards) + heapq.heappop(cards)
        heapq.heappush(cards, sum_value)
        answer += sum_value
    print(answer)
