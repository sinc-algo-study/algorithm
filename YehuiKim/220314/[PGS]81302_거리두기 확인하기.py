# 거리두기 지키면 1, 안지키면 0 담기
# P와 P사이 거리 2이하면 실패.
# 하지만 그 사이 파티션 있다면 성공.=> 가로세로 방향이면 그 사이, 대각선이면 그사이 둘다
# 브루트포스?
def solution(places):
    answer = []
    for room in places:
        answer.append(checkAdj(room))
    return answer


def checkAdj(room):
    dir1 = [(1, 0), (0, 1)]  # dc, dr => 우, 하
    dir2 = [(2, 0), (0, 2), (1, 1), (-1, 1)]  # dc, dr => 우우, 하하, 우하, 좌하
    pplIn2 = [[(1, 0)], [(0, 1)], [(1, 0), (0, 1)], [(-1, 0), (0, 1)]]

    for r in range(5):
        for c in range(5):
            if room[r][c] == "P":
                # 거리 1인 곳에 사람 있는지 확인
                for dc, dr in dir1:
                    nc, nr = c + dc, r + dr
                    if nc >= 5 or nr >= 5:
                        continue
                    # 사람 있으면 실패
                    if room[nr][nc] == "P":
                        return 0
                # 거리 2인 곳에 사람 있는지 확인
                for d in range(4):
                    dc, dr = dir2[d]
                    nc, nr = c + dc, r + dr
                    if nc >= 5 or nr >= 5:
                        continue
                    if room[nr][nc] == "P":
                        for xc, xr in pplIn2[d]:
                            # 칸막이도 없으면 실패
                            if room[r + xr][c + xc] != 'X':
                                return 0
    return 1


# PXPXP
# XPXPO
# POO

places=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))