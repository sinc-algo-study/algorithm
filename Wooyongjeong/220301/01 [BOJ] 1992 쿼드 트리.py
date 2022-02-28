"""
대표적인 분할 정복, 재귀 문제
문제 조건대로 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래를 나누어 풀자
"""


def solution(x, y, n):
    global answer
    # 현재 범위에서 1의 개수를 count
    cnt = 0
    for i in range(x, x + n):
        for j in range(y, y + n):
            if video[i][j] == 1:
                cnt += 1
    if cnt == 0:
        # 현재 범위의 영상이 모두 0인 경우
        answer += "0"
        return
    elif cnt == n * n:
        # 현재 범위의 영상이 모두 1인 경우
        answer += "1"
        return
    # 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래로 나누어 분할 정복
    answer += "("
    half_size = n // 2
    solution(x, y, half_size)          # 왼쪽 위
    solution(x, y + half_size, half_size)      # 오른쪽 위
    solution(x + half_size, y, half_size)      # 왼쪽 아래
    solution(x + half_size, y + half_size, half_size)  # 오른쪽 아래
    answer += ")"


if __name__ == '__main__':
    N = int(input())
    video = [list(map(int, input())) for _ in range(N)]
    answer = ""
    solution(0, 0, N)
    print(answer)
