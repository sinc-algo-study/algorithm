import bisect
from collections import defaultdict

# 효율성에서 실패 -> bisect 써야 통과한다네 (블로그 참고)
# def solution(info, query):
#     candi = defaultdict(list)
#     score = []
#     for i in range(len(info)):
#         x = info[i].split(" ")
#         for k in x[:-1]:
#             candi[k].append(i)
#         score.append(int(x[-1]))
#
#     n = len(query)
#     ans = []
#     for qr in query:
#         x = qr.replace(" and", "").split(" ")
#         res = set(range(len(info)))
#         for k in x[:-1]:
#             if k != '-':
#                 res = res.intersection(candi[k])
#         cnt = 0
#         for r in res:
#             if score[r] >= int(x[-1]):
#                 cnt += 1
#         ans.append(cnt)
#     return ans


def solution(info, query):
    candi = defaultdict(list)

    def make_candi(base, idx, st):
        if idx == 4:
            candi[st].append(int(base[-1]))
            return
        # 모든 조합 고려 ("-" 포함)
        make_candi(base, idx+1, st+base[idx])
        make_candi(base, idx+1, st+"-")

    for i in info:
        x = i.split(" ")
        make_candi(x, 0, "")
        
    for v in candi.values():    # 정렬
        v.sort()

    ans = []
    for qr in query:
        x = qr.split(" ")
        k1 = x[0] + x[2] + x[4] + x[6]  # 요구 조건
        k2 = int(x[7])                  # 요구 점수

        cnt = len(candi[k1]) - bisect.bisect_left(candi[k1], k2)
        ans.append(cnt)
    return ans


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
               , ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

