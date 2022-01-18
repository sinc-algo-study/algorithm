'''
- 도시 : nxn
- (r,c) : r행 c열 => 1, 1부터 시작
- 0: 빈칸, 1: 집, 2: 치킨집
- 최대 m개의 치킨집 => 최!대!

<목표>
: m개 치킨집에 대해 치킨거리의 최솟값 구하기
=> 전체치킨집 갯수로 m개의 조합 만들어서 for문
=> for문 돌면서, 각 집의 치킨거리 구해서
   더하고, 이를 min으로 최솟값 출력되도록
- 순열 : itertools.permutation(list, n)
- 조합 : itertools.combinations(list, n)

<유의>
- 최-대 m개의 치킨집 => 1~m !
- 집개수(최대 100개), 도시크기 최대 50
  => 도시치킨거리는 대략 100*50*2 = 10000 보다는 작을 것이다.
'''

import sys
from itertools import combinations
in_put = sys.stdin.readline


def min_chick_distance(m, houses, chicks):
    total = 10000
    for i in range(1,m+1):
        chick = combinations(chicks, i)
        for chk in chick:
            sub_total = 0
            for h in houses:
                dist = 10000
                for c in chk:
                    temp_dist = abs(c[0] - h[0])+abs(c[1] - h[1])
                    dist = min(dist, temp_dist)
                sub_total += dist
            total = min(total, sub_total)
    return total


if __name__ == '__main__':
    n, m = map(int, in_put().split())
    houses = []
    chicks = []
    for r in range(n):
        col = list(map(int, in_put().split()))
        for c in range(n):
            if col[c] == 1:
                houses.append((r,c))
            elif col[c] == 2:
                chicks.append((r,c))

    print(min_chick_distance(m, houses, chicks))
    