import sys
from queue import PriorityQueue

'''
- 카드묶음  : c1 < c2 < c3 < ...
- 제일 작은 카드묶음 2개 더하기 (c1+c2)
    -> c1+c2값 반영해서 다시 오름차순 정렬 필요
    -> 우선순위큐 사용

1. 우선순위큐 사용
2. 카드묶음 우선순위큐에 put
3. 우선순위큐 길이 1보다 크면, 
    get 2번 해서 더하기
    더한값 우선순위 큐에 put
'''

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
