import sys
import heapq
input = sys.stdin.readline


def go_cave(i):
    heap = []
    map = maps[i]
    n = len(map)
    visited = [[0]*n for _ in range(n)]
    val_map = [[100000]*n for _ in range(n)]

    val_map[0][0] = map[0][0]
    visited[0][0] = 1
    heapq.heappush(heap, (val_map[0][0], 0, 0))
    while heap:
        val, x, y = heapq.heappop(heap)
        if x == n-1 and y == n-1:
            break
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if nx<0 or nx>n-1 or ny<0 or ny>n-1: # 범위 밖이면 패스
                continue
            if visited[ny][nx]:
                continue
            n_val = val + map[ny][nx]
            val_map[ny][nx] = n_val
            visited[ny][nx] = 1
            heapq.heappush(heap, (n_val, nx, ny))
    return str(val)


if '__main__' == __name__:
    n = int(input())
    maps = []
    values = []
    direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 상 하 좌 우

    while 1:
        if n == 0:
            break
        else :
            temp = [list(map(int, input().split())) for _ in range(n)]
            maps.append(temp)
            n = int(input())

    for i in range(len(maps)):
        print("Problem "+str(i+1)+": "+go_cave(i))

