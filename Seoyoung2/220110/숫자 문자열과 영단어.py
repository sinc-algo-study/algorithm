# https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3

def solution(s):
    alpha = {"zero": "0", "one": "1", "two": "2",
             "three": "3", "four": "4", "five": "5",
             "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    ans = []
    while s:
        if s[0].isdigit():
            ans.append(s[0])
            s = s[1:]
        else:
            for k, v in alpha.items():
                if s.startswith(k):
                    ans.append(v)
                    s = s[len(k):]
    return int("".join(ans))


print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))
