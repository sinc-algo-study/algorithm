'''
우선순위큐(heapq) 사용

- 주의 -
숫자 카드 묶음의 크기는 모두 같을 수 있다!!!
ex) 5개 10, 10, 10, 10, 10
'''
import sys
import heapq
in_put = sys.stdin.readline


def heap_card(hp):
    heapq.heapify(hp)
    answer = 0
    first = heapq.heappop(hp)
    if not hp:  # 예외처리
        return 0
    second = heapq.heappop(hp)
    answer += first + second
    heapq.heappush(hp, answer)
    while hp:
        first = heapq.heappop(hp)
        second = heapq.heappop(hp)
        sub_ans = first + second
        answer += sub_ans
        if not hp:
            return answer
        heapq.heappush(hp, sub_ans)
    return answer


if __name__ == '__main__':
    n = int(in_put())
    hp = [int(in_put().rstrip()) for _ in range(n)]
    print(heap_card(hp))
