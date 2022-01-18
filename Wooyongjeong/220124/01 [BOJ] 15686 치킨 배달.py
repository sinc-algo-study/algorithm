"""
1. 도시에서 집, 치킨집 좌표 정보를 각각 구함
2. 치킨집 중 M개를 골라(조합으로) 각 치킨집의 '치킨 거리'를 구해 정답 갱신
    치킨 거리: 집과 가장 가까운 치킨집 사이의 거리. '집'을 기준으로 정해짐
"""
from itertools import combinations


def get_distance(home_x, home_y, place_x, place_y):
    return abs(home_x - place_x) + abs(home_y - place_y)


def solution(n, m, board):
    # 중첩 함수를 이용, homes를 파라미터로 안 넘겨줘도 되도록 했음
    def get_chicken_distance(places):
        # 각 집마다 모든 치킨 집과의 거리를 재보고, 가장 작은 값으로 치킨 거리를 확정
        # 각 집의 치킨 거리를 모두 더한 값 반환
        distance = 0
        for home_x, home_y in homes:
            tmp = INF
            for place_x, place_y in places:
                tmp = min(tmp, get_distance(home_x, home_y, place_x, place_y))
            distance += tmp
        return distance

    homes = []
    chicken_places = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                homes.append((i, j))
            elif board[i][j] == 2:
                chicken_places.append((i, j))

    answer = INF
    candidates = combinations(chicken_places, m)
    for candidate in candidates:
        chicken_distance = get_chicken_distance(candidate)
        answer = min(answer, chicken_distance)
    return answer


if __name__ == '__main__':
    INF = int(1e9)
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, M, city))
