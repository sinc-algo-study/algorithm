from collections import defaultdict
import bisect


def solution(words, queries):
    dict = defaultdict(list)
    redict = defaultdict(list)
    for w in words:
        n = len(w)
        dict[n].append(w)
        redict[n].append(w[::-1])

    # bisect를 위해 sort
    for k in dict:
        dict[k].sort()
        redict[k].sort()

    ans = []
    for q in queries:
        if q[0] == "?":
            x = redict[len(q)]
            aq, zq = q[::-1].replace("?", "a"), q[::-1].replace("?", "z")
        else:
            x = dict[len(q)]
            aq, zq = q.replace("?", "a"), q.replace("?", "z")
        cnt = bisect.bisect_right(x, zq) - bisect.bisect_left(x, aq)
        ans.append(cnt)
    return ans


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))