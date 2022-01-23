import bisect


def count_by_range(iterable, left_value, right_value):
    left_index = bisect.bisect_left(iterable, left_value)
    right_index = bisect.bisect_right(iterable, right_value)
    return right_index - left_index


def make_notes(words):
    SIZE = 100000

    word_note = [[] for _ in range(SIZE + 1)]
    reversed_word_note = [[] for _ in range(SIZE + 1)]

    for word in words:
        word_note[len(word)].append(word)
        reversed_word_note[len(word)].append(word[::-1])

    for length in range(2, SIZE + 1):
        word_note[length].sort()
        reversed_word_note[length].sort()

    return word_note, reversed_word_note


def solution(words, queries):
    answer = []
    word_note, reversed_word_note = make_notes(words)

    for query in queries:
        if not query.startswith('?'):
            count = count_by_range(word_note[len(query)],
                                   query.replace('?', 'a'),
                                   query.replace('?', 'z'))
        else:
            count = count_by_range(reversed_word_note[len(query)],
                                   query[::-1].replace('?', 'a'),
                                   query[::-1].replace('?', 'z'))
        answer.append(count)

    return answer


if __name__ == '__main__':
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    query = ["fro??", "????o", "fr???", "fro???", "pro?"]
    print(solution(words, query))  # [3, 2, 4, 1, 0]
