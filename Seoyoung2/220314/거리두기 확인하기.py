from itertools import combinations
from collections import deque


def solution(places):
    def bfs(st, end):
        visit = set(st)
        q = deque([(st, 0)])
        while q:
            (x, y), cnt = q.popleft()
            if x == end[0] and y == end[1]:
                return False if cnt > 2 else True
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                    continue
                if place[nx][ny] != 'X' and (nx, ny) not in visit:
                    q.append(((nx, ny), cnt + 1))
                    visit.add((nx, ny))
        return False

    ans = [1] * 5
    for idx, place in enumerate(places):
        # place = ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]
        pos = [(x, y) for x in range(5) for y in range(5) if place[x][y] == 'P']
        for p1, p2 in combinations(pos, 2):
            # 거리 확인
            if abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) <= 2:
                if bfs(p1, p2):
                    ans[idx] = 0
                    break
    return ans

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
