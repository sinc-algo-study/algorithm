import collections
import itertools
import bisect


def make_info_dict(info):
    info_dict = collections.defaultdict(list)
    for i in info:
        i = i.split()
        data, score = i[:-1], int(i[-1])
        info_dict[''.join(data)].append(score)
        for count in range(1, 5):
            for indexes in itertools.combinations(range(4), count):
                copied_data = data[:]
                for index in indexes:
                    copied_data[index] = '-'
                info_dict[''.join(copied_data)].append(score)

    for value in info_dict.values():
        value.sort()

    return info_dict


def solution(info, query):
    info_dict = make_info_dict(info)
    answer = []
    for q in query:
        q = [x for x in q.split() if x != 'and']
        key, score = ''.join(q[:-1]), int(q[-1])
        count = len(info_dict[key]) - bisect.bisect_left(info_dict[key], score)
        answer.append(count)
    return answer


if __name__ == '__main__':
    info = ["java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100",
             "python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250",
             "- and backend and senior and - 150",
             "- and - and - and chicken 100",
             "- and - and - and - 150"]
    print(solution(info, query))  # [1, 1, 1, 1, 2, 4]
