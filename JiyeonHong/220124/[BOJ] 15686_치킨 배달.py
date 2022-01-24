from itertools import combinations
'''
치킨집 최대 M개만 남길 경우, 도시 치킨거리의 최솟값 구하기
-> 조합 사용

1. 치킨집, 집의 좌표 리스트에 저장
2. 치킨집 M개 선택하는 조합 구하기
3. 각 조합마다 도시치킨거리 구하기
'''
def solution(city, M):
    # 치킨집, 집 좌표 찾기
    chickens = []
    houses = []
    for r in range(len(city)):
        for c in range(len(city)):
            if city[r][c] == 2:
                chickens.append((r, c))
            if city[r][c] == 1:
                houses.append((r, c))

    chickensComb = list(combinations(chickens, M))

    # 치킨집 M개 고를 경우, 도시치킨거리 최솟값 구하기
    cityDist = 100 * 50 * 50 * 13
    for comb in chickensComb:
        dist = 0  # 각 조합의 치킨 거리
        for ht in houses:
            houseDist = 100
            r1, c1 = ht
            for ct in comb:
                r2, c2 = ct
                houseDist = min(houseDist, abs(r1 - r2) + abs(c1 - c2))
            dist += houseDist

        cityDist = min(cityDist, dist)

    return cityDist


if __name__ == '__main__':
    N, M = map(int, input().split())
    city = []
    for _ in range(N):
        city.append(list(map(int, input().split())))

    print(solution(city, M))
