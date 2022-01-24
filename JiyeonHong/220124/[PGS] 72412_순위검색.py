from itertools import combinations

'''
1. dict = key(지원조건조합) : value(해당 조건의 지원자 점수)
2. info 원소 하나마다 만들 수 있는 모든 조합 만들기
    -> info 하나당 4C0+4C1+4C2+4C3+4C4=16개의 조합
3. dict key 마다 value 오름차순으로 정렬
4. query에서 '-' 제거 -> dict에서 제거해서 key로 설정했기 때문
5. 이진탐색으로 X점 이상인 첫 인덱스 찾기 
'''


def solution(infos, queries):
    answer = []

    info_dict = {}
    for info in infos:
        info = info.split(' ')
        info_key = info[:-1]
        info_val = int(info[-1])
        # info에서 16가지 경우의 수 만들기
        for i in range(5):
            for c in combinations(info_key, i):
                key = ''.join(c)  # 튜플->문자열
                info_dict.setdefault(key, []).append(info_val)

    print(info_dict)

    # 각 키마다 점수 정렬
    for key in info_dict.keys():
        info_dict[key].sort()

    for query in queries:
        query = query.replace('and ', '').split(' ')
        score = int(query[-1])
        query = query[:-1]
        queryStr = ''.join(query)  # 리스트->문자열
        condition = queryStr.replace('-', '')

        if condition in info_dict:
            info_scores = info_dict[condition]
            if len(info_scores) > 0:
                # 이진 탐색
                start = 0
                end = len(info_scores) - 1

                while start <= end:
                    mid = (start + end) // 2

                    if info_scores[mid] < score:
                        start = mid + 1
                    else:
                        end = mid - 1
                answer.append(len(info_scores) - start)
        else:
            answer.append(0)

    return answer


if __name__ == '__main__':
    info = ["java backend junior pizza 150", "python frontend senior chicken 210",
            "python frontend senior chicken 150", "cpp backend senior pizza 260",
            "java backend junior chicken 80", "python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100",
             "python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250",
             "- and backend and senior and - 150",
             "- and - and - and chicken 100",
             "- and - and - and - 150"]
    print(solution(info, query))
