import collections


def solution(n, s, sequence):
    global answer
    sum_dict = collections.defaultdict(int)

    def dfs_left(i, sum_value):
        if i == n // 2:
            sum_dict[sum_value] += 1
            return

        dfs_left(i + 1, sum_value)
        dfs_left(i + 1, sum_value + sequence[i])

    def dfs_right(i, sum_value):
        global answer
        if i == n:
            answer += sum_dict[s - sum_value]
            return

        dfs_right(i + 1, sum_value)
        dfs_right(i + 1, sum_value + sequence[i])

    dfs_left(0, 0)
    dfs_right(n // 2, 0)

    if s == 0:
        answer -= 1


if __name__ == '__main__':
    N, S = map(int, input().split())
    sequence = list(map(int, input().split()))
    answer = 0
    solution(N, S, sequence)
    print(answer)
