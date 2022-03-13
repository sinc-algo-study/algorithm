def solution(n, arr):
    # dp 배열에는 arr[0] ~ arr[i]까지의 연속합 중 최댓값을 저장
    # dp[i][0]: 범위 [0, i]에서 어느 것도 제거하지 않았을 경우에 최댓값
    # dp[i][1]: 범위 [0, i]에서 하나의 수를 삭제하였을 경우에 최댓값
    dp = [[-int(1e9)] * 2 for _ in range(n)]
    dp[0][0] = arr[0]
    dp[0][1] = arr[0]

    answer = arr[0]

    for i in range(1, n):
        # 제거하지 않아야 하므로
        # 범위 [0, i] 연속합 (dp[i - 1][0] + arr[i]) or
        # i번째 원소 (arr[i]) 중 최댓값으로 결정
        dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i])
        # 수 하나를 제거했을 때 최댓값을 구해야되니까
        # i번째 수를 제거했을 때의 최댓값 (dp[i - 1][0]) or
        # i번째 수가 아닌 다른 수를 제거했을 때의 최댓값 (dp[i - 1][1] + arr[i])
        # 중에서 최댓값으로 결정
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + arr[i])
        answer = max(answer, dp[i][0], dp[i][1])

    return answer


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(solution(n, arr))
