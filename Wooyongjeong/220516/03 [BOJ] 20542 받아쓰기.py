def check(char1, char2):
    return char1 == char2 or \
            (char1 == 'v' and char2 == 'w') or \
            (char1 == 'i' and char2 in ['j', 'l'])


def solution(word1, word2):
    dp = [[i] + [0] * M for i in range(N + 1)]
    dp[0] = [i for i in range(M + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            if check(word1[i - 1], word2[j - 1]):
                dp[i][j] = dp[i - 1][j - 1]

    return dp[N][M]


if __name__ == '__main__':
    N, M = map(int, input().split())
    word1 = input()
    word2 = input()
    print(solution(word1, word2))
