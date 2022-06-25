def can_read(word, taught):
    for alphabet in word:
        i = ord(alphabet) - ord('a')
        if not taught[i]:
            return 0
    return 1


def get_readable_cnt(words, taught):
    cnt = 0
    for word in words:
        cnt += can_read(word, taught)
    return cnt


def dfs(k, index, taught, words):
    global answer
    if k == 0:
        cnt = get_readable_cnt(words, taught)
        answer = max(answer, cnt)
        return

    for i in range(index, SIZE):
        if taught[i]:
            continue

        taught[i] = True
        dfs(k - 1, i, taught, words)
        taught[i] = False


def solution(k, words):
    # 모든 단어가 'anta'로 시작해 'tica'로 끝나기 때문에
    # 'a', 'c', 't', 'i', 'n'은 알고 있어야 함
    taught = [False] * SIZE
    for alphabet in list(set('antatica')):
        taught[ord(alphabet) - ord('a')] = True

    dfs(k - 5, 0, taught, words)


if __name__ == '__main__':
    SIZE = 26
    N, K = map(int, input().split())
    words = [input() for _ in range(N)]
    if K < 5:
        print(0)
    elif K == SIZE:
        print(N)
    else:
        answer = 0
        solution(K, words)
        print(answer)
