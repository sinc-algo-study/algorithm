


def solution(s):
    answer = 0
    map = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    key = ""
    lst = []
    for ch in s:
        if ch.isdigit():
            lst.append(ch)
        else:
            key += ch
            if key in map.keys():
                lst.append(map.get(key))
                key = ""

    answer = int("".join(lst))
    return answer



if __name__ == '__main__':
    ss = ["one4seveneight", "23four5six7", "2three45sixseven", "123"]
    for s in ss:
        print(s, solution(s))