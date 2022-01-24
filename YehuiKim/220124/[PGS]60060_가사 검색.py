from bisect import bisect_right, bisect_left

# 시간초과된 풀이
def my_solution(words, queries):
    words.sort()
    reversed_w = []
    for w in words:
        reversed_w.append(w[::-1])
    reversed_w.sort()

    answer = []
    for q in queries:
        leng = len(q)
        cnt = 0
        if q.startswith('?'):
            q = q[::-1].strip("?")
            left = bisect_left(reversed_w,q)
            right = bisect_left(reversed_w,chr(ord(q[0])+1))
            for i in range(left, right):
                if len(reversed_w[i]) != leng:
                    continue
                else :
                    if reversed_w[i].startswith(q):
                        cnt += 1

        else:
            q = q.strip("?")
            left = bisect_left(words,q)
            right = bisect_left(words,chr(ord(q[0])+1))
            for i in range(left, right):
                if len(words[i]) != leng:
                    continue
                else :
                    if words[i].startswith(q):
                        cnt += 1

        answer.append(cnt)
    return answer

# 검증안된 풀이 (시간부족으로 아이디어만 담아봄)
class Trie:
    # 한 인스턴스 한정으로, 글로벌하게 사용되는 변수
    head = {'val':0, 'length':[], 'ch':{}}
    cnt = 0

    def insert(self, word):
        cur = self.head
        for c in word:
            if c not in cur['ch']:
                cur['ch'][c]={'val':0, 'length':[len(word)], 'ch':{}}
            cur = cur['ch'][c]
        cur['val'] += 1
        cur['length'].append(len(word))

    def search(self, word, leng):
        cur = self.head
        for w in word:
            if w not in cur['ch']:
                return 0
            cur = cur['ch'][w]
        len_list = cur['length']
        len_list.sort()
        return bisect_right(len_list, leng)-bisect_left(len_list, leng)

def solution(words, queries):
    trie1 = Trie()
    trie2 = Trie()
    answer = []

    for w in words:
        trie1.insert(w)
        trie2.insert(w[::-1])
    for q in queries:
        cnt = 0
        leng = len(q)
        if q.startswith('?'):
            q = q.strip("?")
            cnt = trie2.search(q[::-1], leng)
            answer.append(cnt)
        else :
            q = q.strip('?')
            cnt = trie1.search(q[::-1], leng)
            answer.append(cnt)
    return answer

if __name__ == '__main__' :
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    print(solution(words, queries))