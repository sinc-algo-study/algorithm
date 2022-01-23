from bisect import bisect_left


def solution(info, query):
    # 구조 만들기
    people = [ [ [ [[], []], [[], []] ], [ [[], []], [[], []] ] ],\
               [ [ [[], []], [[], []] ], [ [[], []], [[], []] ] ],\
               [ [ [[], []], [[], []] ], [ [[], []], [[], []] ] ] ]

    # 지원자 분류하기
    for p in info:
        temp = list(p.split())
        if temp[0] == 'cpp':
            a = 0
        elif temp[0] == 'java':
            a = 1
        elif temp[0] == 'python':
            a = 2
        if temp[1] == 'backend':
            b = 0
        elif temp[1] == 'frontend':
            b = 1
        if temp[2] == 'junior':
            c = 0
        elif temp[2] == 'senior':
            c = 1
        if temp[3] == 'chicken':
            d = 0
        elif temp[3] == 'pizza':
            d = 1
        people[a][b][c][d].append(int(temp[4]))

    # n차 배열 내의 점수 정렬하기
    for i_1 in range(3):
        for i_2 in range(2):
            for i_3 in range(2):
                for i_4 in range(2):
                    people[i_1][i_2][i_3][i_4].sort()

    # 쿼리에 따라 카운트
    answer = []
    for q in query:
        q_temp = q.split(' and ')
        q_temp += q_temp.pop().split()
        if q_temp[0] == 'cpp':
            a = [0]
        elif q_temp[0] == 'java':
            a = [1]
        elif q_temp[0] == 'python':
            a = [2]
        else:
            a = [0, 1, 2]

        if q_temp[1] == 'backend':
            b = [0]
        elif q_temp[1] == 'frontend':
            b = [1]
        else:
            b = [0, 1]

        if q_temp[2] == 'junior':
            c = [0]
        elif q_temp[2] == 'senior':
            c = [1]
        else:
            c = [0, 1]

        if q_temp[3] == 'chicken':
            d = [0]
        elif q_temp[3] == 'pizza':
            d = [1]
        else:
            d = [0, 1]

        res = 0
        for aa in a:
            for bb in b:
                for cc in c:
                    for dd in d:
                        now = people[aa][bb][cc][dd]
                        res += len(now) - bisect_left(now, int(q_temp[4]))
        answer.append(res)
    return answer


if __name__ == '__main__':
    info = ["java backend junior pizza 150",\
            "python frontend senior chicken 210",\
            "python frontend senior chicken 150",\
            "cpp backend senior pizza 260",\
            "java backend junior chicken 80",\
            "python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100",\
             "python and frontend and senior and chicken 200",\
             "cpp and - and senior and pizza 250",\
             "- and backend and senior and - 150",\
             "- and - and - and chicken 100",\
             "- and - and - and - 150"]
    print(solution(info, query))