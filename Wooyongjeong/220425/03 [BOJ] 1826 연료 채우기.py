"""
주유소 개수 N <= 1만
백트래킹은 당연히 안됨

주유소에 멈추는 횟수를 최소화 하고 싶다
-> 갈 수 있는 주유소 중 기름을 가장 많이 넣을 수 있는 주유소에서 멈춘다?
-> heapq 이용해서 정렬
"""
import heapq


def solution(fuel_left: int, dest: int, gas_station: list[list[int]]) -> int:
    """
    data는 (주유소 까지의 거리, 연료 양) 기준으로 min heap
    """
    answer = 0
    heap = []

    while fuel_left < dest:
        # 아직 주유소가 남아 있고, 남은 연료로 해당 주유소까지 갈 수 있을 때까지 반복
        while gas_station and gas_station[0][0] <= fuel_left:
            dist, fuel_amount = heapq.heappop(gas_station)
            # 주유할 수 있는 연료 양 기준으로 max heap 만듬
            heapq.heappush(heap, (-fuel_amount, dist))

        if not heap:
            # 현재 남아 있는 연료로 주유소까지 갈 수 없다 == 마을까지도 못 간다
            return -1

        # 가장 많은 기름을 넣을 수 있는 주유소에서 멈춤
        fuel_amount, dist = heapq.heappop(heap)
        fuel_amount *= -1

        fuel_left += fuel_amount
        answer += 1

    return answer


if __name__ == '__main__':
    N = int(input())
    data = []
    for _ in range(N):
        heapq.heappush(data, list(map(int, input().split())))
    L, P = map(int, input().split())
    print(solution(P, L, data))
