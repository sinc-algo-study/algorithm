'''
1. words에서 단어길이별로 단어 dictionary에 저장
2. query 길이를 key로 dictionary에서 찾기
3. query에서 와일드카드 뺀 문자열 구하기
4. startswith, endswith로 query랑 일치하는 word 갯수 구하기
'''

def solution(words, queries):
    answer = []

    # key: 단어 길이, value : 단어
    word_dict = {}
    for word in words:
        key = len(word)
        word_dict.setdefault(key, []).append(word)

    for query in queries:
        key = len(query)
        find = ''
        # 검색 키워드랑 같은 길이의 words
        if key in word_dict:
            find_words = word_dict[key]
        else:
            answer.append(0)
            continue

        count = 0
        if query.startswith('?'):  # ex. ????o
            # 검색 키워드에서 소문자만 갖고오기
            for i in range(len(query)):
                if query[i] != '?':
                    find = query[i:]
                    break

            for word in find_words:
                if word.endswith(find):
                    count += 1

        else:  # fro??
            for i in range(len(query)):
                if query[i] == '?':
                    find = query[:i]
                    break

            for word in find_words:
                if word.startswith(find):
                    count += 1

        answer.append(count)
    return answer

if __name__=='__main__':
    words=["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries=["fro??", "????o", "fr???", "fro???", "pro?"]
    print(solution(words,queries))