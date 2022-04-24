"""
N <= 10만으로, O(N^2)으로는 안됨
투 포인터 써서 O(N)으로
"""
import collections


def solution(gems):
    answer = []

    shortest = len(gems) + 1
    start, end = 0, 0

    all_kind = len(set(gems))
    gems_dict = collections.defaultdict(int)

    while end < len(gems):
        gems_dict[gems[end]] += 1
        end += 1

        if len(gems_dict) == all_kind:
            while start < end:
                if gems_dict[gems[start]] > 1:
                    gems_dict[gems[start]] -= 1
                    start += 1
                elif shortest > end - start:
                    shortest = end - start
                    answer = [start + 1, end]
                    break
                else:
                    break

    return answer


if __name__ == '__main__':
    gems_list = [
        ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
        ["AA", "AB", "AC", "AA", "AC"],
        ["XYZ", "XYZ", "XYZ"],
        ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
    ]

    for gems in gems_list:
        print(solution(gems))
