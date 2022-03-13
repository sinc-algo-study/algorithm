import itertools


SIZE = 5


def get_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_not_keeping_distance_candidates(room):
    interviewers = []

    for i in range(SIZE):
        for j in range(SIZE):
            if room[i][j] == 'P':
                interviewers.append((i, j))

    candidates = []
    for i1, i2 in itertools.combinations(interviewers, 2):
        distance = get_distance(i1, i2)
        if distance <= 2:
            candidates.append((i1, i2))
    return candidates


def is_diagonal(i1, i2):
    return i1[0] != i2[0] and i1[1] != i2[1]


def get_partitions_count(room, i1, i2):
    x1 = min(i1[0], i2[0])
    y1 = min(i1[1], i2[1])
    x2 = max(i1[0], i2[0])
    y2 = max(i1[1], i2[1])

    cnt = 0
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if room[x][y] == 'X':
                cnt += 1
    return cnt


def is_keeping_distance(room):
    candidates = get_not_keeping_distance_candidates(room)
    for i1, i2 in candidates:
        diagonal = is_diagonal(i1, i2)
        partitions_count = get_partitions_count(room, i1, i2)
        if diagonal and partitions_count < 2:
            return 0
        if not diagonal and partitions_count < 1:
            return 0
    return 1


def solution(places):
    answer = []

    for place in places:
        room = [list(p) for p in place]
        answer.append(is_keeping_distance(room))

    return answer


if __name__ == '__main__':
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
              ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
              ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
              ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
              ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solution(places))
