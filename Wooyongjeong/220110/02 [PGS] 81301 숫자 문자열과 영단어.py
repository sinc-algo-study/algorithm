def solution(s):
    # 각 숫자를 index로 해서 영단어 list 생성
    words = ["zero", "one", "two", "three", "four", "five", "six",
             "seven", "eight", "nine"]
    for i in range(10):
        # 각 숫자마다 replace 함수 이용해서 영단어 -> 숫자로 변경
        s = s.replace(words[i], str(i))
    return int(s)


if __name__ == '__main__':
    ss = ["one4seveneight", "23four5six7", "2three45sixseven", "123"]
    for s in ss:
        print(s, solution(s))
