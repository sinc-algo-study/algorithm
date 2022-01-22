'''

0 : 빈캄
1 : 집
2 : 치킨집

치킨집 M개만을 남겨 치킨거리의 최소값을 달성하라  XXXXXX
->
1. 치킨집 좌표를 리스트 하나로 관리
2. 리스트에서 M개 구하는 모든 조합 생성
3. 각 조합 별 치킨 거리의 합 계산

입력


자바에선 Pair 클래스를 만들어서 사용했었는데.. 파이썬에선 어떻게?
-> 튜플 사용

N(2 ≤ N ≤ 50), M(1 ≤ M ≤ 13

'''

# from itertools import combinations
#
# def solution():
#     # 치킨집 좌표를 리스트로 관리
#     chicken_positions = [(i, j) for i in range(N) for j in range(M) if board[i][j] == 2]
#     # 치킨집이 없는 board
#     without_chicken = [board[i][j] if board[i][j] != 2 else 0 for i in range(N) for j in range(M)]
#
#     # 치킨집 좌표들의 조합
#     comb = list(combinations(chicken_positions, M))
#
#
#     '''
#     그냥 처음 입력받을때 이중for문으로 받아서 한 번에 구하는 게 좋을듯??
#     '''
#
#
#     pass
#
#
#
# if __name__ == '__main__':
#     N, M = map(int, input().split())
#     board = [list(map(int, input().split())) for _ in range(N)]
#
#
#
#     solution()


from itertools import combinations
import copy
import sys
input = sys.stdin.readline


def calc_distance(copied_board, comb):
    ans = 0  # 집에서 가장 가까운 치킨 거리의 합

    for h in house_positions:
        hr, hc = h[0], h[1]
        min_dist = N + N

        for chicken in comb:
            cr, cc = chicken[0], chicken[1]
            dist = abs(hr - cr) + abs(hc - cc)
            min_dist = min(min_dist, dist)
            if min_dist == 1:
                break

        ans += min_dist

    return ans


def solution(num):
    ans = (N + N) * len(house_positions)
    chicken_combs = list(combinations(chicken_positions, num))

    for comb in chicken_combs:
        # comb = ((), (), () ... ())
        # 질문 : 이전 반복에서 쓰였던 copied_board는? 메모리 회수 제대로 되는건가?
        copied_board = copy.deepcopy(board)

        for t in comb:
            r, c = t[0], t[1]
            copied_board[r][c] = 2

        # 이제 치킨 거리의 합을 구한다
        chicken_distance = calc_distance(copied_board, comb)  # 하나의 조합에 대한 치킨 거리의 합
        ans = min(ans, chicken_distance)

    return ans


if __name__ == '__main__':
    N, M = map(int, input().split())
    board = []
    chicken_positions = []
    house_positions = []

    for i in range(N):
        input_list = list(map(int, input().split()))

        for j in range(N):
            if input_list[j] == 2:
                input_list[j] = 0
                chicken_positions.append((i, j))
            elif input_list[j] == 1:
                house_positions.append((i, j))

        board.append(input_list)

    print(solution(M))
