"""
stones 배열 크기 20만
stones 각 원소 값 최대 2억

범위가 매우 크다 -> 이진 탐색..?

mid : 징검다리를 건너는 친구들의 수
로 놓고 이진탐색 진행
"""


def solution(stones, k):
    def check(n):
        # n-1명은 다 건넜다고 가정하고,
        # 숫자가 0인 돌이 연속으로 k개인지 확인
        cnt = k
        for stone in stones:
            if stone < n:
                cnt -= 1
            else:
                cnt = k
            if cnt == 0:
                return False
        return True

    left = 1
    right = max(stones) + 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if check(mid):
            left = mid
        else:
            right = mid
    return left


if __name__ == '__main__':
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    print(solution(stones, k))
