import sys
from queue import PriorityQueue


def solution(sizes):
    sizes.sort()
    answer = 0

    pq = PriorityQueue()
    for size in sizes:
        pq.put(size)

    answer = 0
    while pq.qsize()>1:
        sum = pq.get() + pq.get()
        pq.put(sum)
        answer += sum

    return answer


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    sizes = [int(sys.stdin.readline()) for _ in range(N)]
    print(solution(sizes))
