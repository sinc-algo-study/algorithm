# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3


def solution(s):
    n = len(s)
    ans = 1000
    for i in range(1, n//2+1):  # 패턴의 길이
        pt = s[:i]
        cnt = 1
        tmp = ""
        for j in range(i, n+i, i):
            if pt == s[j:j+i]:
                cnt += 1
            else:   # 패턴 불일치
                if cnt == 1:
                    tmp += pt
                else:
                    tmp += (str(cnt) + pt)
                pt = s[j:j+i]   # pattern 교체
                cnt = 1
        ans = min(ans, len(tmp))
    return 1 if n == 1 else ans


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("a"))

