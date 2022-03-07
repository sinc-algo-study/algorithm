"""
0. 기둥 or 보를 설치 or 삭제 할 때마다 가능한지 체크
1. 설치
    1-1. answer에 [x, y, a] append
    1-2. 불가능하면 answer에서 remove
2. 삭제
    1-1. answer에서 [x, y, a] remove
    1-2. 불가능하면 다시 answer에 [x, y, a] append

가능한지 체크
1. 기둥, 보 각각 문제 조건과 부합하는지 체크
"""


def is_possible(frames):
    for frame in frames:
        x, y, a = frame
        if a == 0:  # 기둥
            # 1. 바닥 위에 있거나
            # 2. 보의 한쪽 끝 부분 위에 있거나,
            # 3. 또는 다른 기둥 위에 있어야 합니다.
            if y == 0 or \
                    [x - 1, y, 1] in frames or [x, y, 1] in frames or \
                    [x, y - 1, 0] in frames:
                continue
            return False
        else:  # 보
            # 1. 한쪽 끝 부분이 기둥 위에 있거나,
            # 2. 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
            if [x, y - 1, 0] in frames or [x + 1, y - 1, 0] in frames or \
                    ([x - 1, y, 1] in frames and [x + 1, y, 1] in frames):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        # x, y: 기둥, 보를 설치 또는 삭제할 교차점의 좌표
        # a: 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보
        # b: 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치
        x, y, a, b = frame
        if b == 0:  # 삭제
            answer.remove([x, y, a])
            if not is_possible(answer):
                answer.append([x, y, a])
        else:  # 설치
            answer.append([x, y, a])
            if not is_possible(answer):
                answer.remove([x, y, a])
    return sorted(answer)


if __name__ == '__main__':
    n = 5
    build_frames = [
        [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1],
         [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]],
        [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1],
         [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
    ]
    for build_frame in build_frames:
        print(solution(n, build_frame))
