'''

query를 만족하는 word의 개수를 구하라.

queries[i]는 와일드카드 '?'를 포함한다.

(words)
words 길이 : 2 ~ 100,000
words[i] 길이(단어 길이) : 1 ~ 10,000
모든 원소의 길이의 합 : 2 ~ 1,000,000
※ 1. words에서 중복되는 원소는 없음
  2. 알파벳 소문자로만 구성됨

(queries)
queries 길이 : 2 ~ 100,000
queries[i] 길이 : 1 ~ 10,000
모든 원소의 길이의 합 : 2 ~ 1,000,000
※ 1. 알파벳 소문자 + '?' 로만 구성됨
  2. '?'는 반드시 하나 이상 포함됨
  3. '?'는 반드시 접두사 or 접미사 (접두사 and 접미사 -> 없음)


대충 봐도 브루트 포스는 절대 불가...
100,000 * 100,000 이상이다..

'''


from bisect import bisect_left, bisect_right


def count_by_range(iterable, left_value, right_value):
    left_index = bisect_left(iterable, left_value)
    right_index = bisect_right(iterable, right_value)
    return right_index - left_index


def init_list(words):
    # word의 길이를 기준으로 각 배열에서 따로 관리 한다
    word_list = [[] for _ in range(10001)]
    reversed_word_list = [[] for _ in range(10001)]

    for word in words:
        size = len(word)
        word_list[size].append(word)
        reversed_word_list[size].append(word[::-1])

    # 이진 탐색을 위해 정렬
    for i in range(1, 10001):
        word_list[i].sort()
        reversed_word_list[i].sort()

    return word_list, reversed_word_list


def solution(words, queries):
    answer = []

    word_list, reversed_word_list = init_list(words)

    # 알파벳으로 시작해야만 이진탐색을 할 수 있다
    for query in queries:
        size = len(query)
        if query.startswith('?'):
            cnt = count_by_range(reversed_word_list[size],
                                 query[::-1].replace('?', 'a'),
                                 query[::-1].replace('?', 'z'))
        else:
            cnt = count_by_range(word_list[size],
                                 query.replace('?', 'a'),
                                 query.replace('?', 'z'))
        answer.append(cnt)

    return answer


if __name__ == '__main__':
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    print(solution(words, queries))  # [3, 2, 4, 1, 0]