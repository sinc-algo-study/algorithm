import sys
in_put = sys.stdin.readline


def check_word(w):
    first = w[:len(w) // 2]
    last = w[(len(w) + 1) // 2:]  # 홀수면, 중간문자 기준 이후
    if first == last[::-1]:  # 회문
        return True
    else:
        return False


def check_usa_word(w):
    left = 0
    right = len(w)-1
    while left<right:
        if w[left] == w[right]:
            left += 1
            right -= 1
        else:
            for i in [left, right]:
                temp = w[:i]+w[i+1:]
                if check_word(temp): # 유사회문
                    return True
            return False


if '__main__' == __name__ :
    n = int(in_put().strip())
    words = []
    answer = []
    for _ in range(n):
        words.append(in_put().strip())

    for w in words:
        if check_word(w):
            print(0)
        else :
            if check_usa_word(w):
                print(1)
            else :
                print(2)