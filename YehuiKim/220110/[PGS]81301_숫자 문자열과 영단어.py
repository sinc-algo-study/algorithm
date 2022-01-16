# - 조건
#     - 영어 ⇒ 숫자로
#     - 숫자 ⇒ 그대로 숫자
# - 풀이핵심
#     - 숫자는 그대로 가져오고
#     - 영어는 영단어 리스트의 원소와 비교하여 같으면, 숫자로 변환하여 가져오기

from collections import deque

def check(tmp):
    while len(tmp) != 0:
        tp = tmp.popleft() + tmp.popleft()
        for i in range(10):
            if tp ==''.join(num[i][0:2]):
                cnt = len(num[i])
                for _ in range(cnt-2):
                    tp = tp + tmp.popleft()
                ans.append(str(i))
                break

def solution(s):
    global num
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    arr = list(s)
    global ans
    ans = []
    tmp = deque()
    for i in arr:
        if i.isdigit():  #숫자
            check(tmp)
            ans.append(i)
        else: #문자
            tmp.append(i)
    check(tmp)
    return int(''.join(ans))