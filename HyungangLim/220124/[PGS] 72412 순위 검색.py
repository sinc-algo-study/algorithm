'''

조건을 만족하는 사람 중 X점 이상인 사람
조건 기준
1. 언어
2. 직군
3. 경력
4. 푸드
+ 점수 (이상 조건만 존재)



info를 점수를 기준으로 정렬하자
이후 query에서 점수를 보고 해당 점수 이상인 것부터 네가지 조건에 대해 검사
근데 query의 점수가 최소 점수라서 모든 info를 봐야하면? 결국 시간복잡도는 똑같은 거 아닌가 그럼?

ㄴㄴㄴㄴㄴ...... 아무리 생각해도 이건 아님.


50,000 * 100,000 = 50억.. 브루트포스 절대 불가.
조회 시간을 줄여야 한다 -> hashmap 사용
key를 어떻게 정할 것인가? -> key:value = 조건:숫자

리드미에서 이진탐색이라는 키워드를 봐버림... 이진탐색을 써야하나? 어디에 써야하지?
걍 해시로 조회하면 되는 거 아닌가???

조건
1. 언어 : cpp, java, python
2. 직군 : backend, frontend
3. 경력 : junior, senior
4. 푸드 : chicken, pizza
5. 점수 : 경우의 수가 너무 많아서 하나하나 다 key로 만드는 것은 무리일 듯.
-> 1~4 조건의 모든 경우의 수의 key를 생성. 각 조건에 해당하는 value는 점수값을 담는 리스트로 하자.

일단 조건에 대해 keySet을 만들어야 함
-> 4 * 3 * 3 * 3 = 108개의 key 존재 (아무것도 안 고르는 경우도 존재한다)


아!! value값인 list를 오름차순 정렬하고 이진탐색으로 해당 점수를 빠르게 구하면 됨!!
hashmap으로 한 번 줄이고, 이진탐색으로 또 한 번 줄이고

'''

# from bisect import bisect_left
#
#
# def solution(info, query):
#     answer = []
#
#     '''
#     모든 조합에 대해 문자열 키를 어떻게 만들지?
#     info에서 받아와서 만드는 게 아니라 그냥 직접 리스트 만들어서 쓰면 되잖아.
#     '''
#
#     langs = ["", "cpp", "java", "python"]
#     tasks = ["", "backend", "frontend"]
#     careers = ["", "junior", "senior"]
#     foods = ["", "chicken", "pizza"]
#     conditions = {}
#
#     # 질문 : 문자열 합칠 때, += 쓰는 게 좋은지? 이렇게 리스트로 만들어서 join 쓰는 게 좋은지?
#     for i in range(len(langs)):
#         condition_unit = [langs[i]]
#         for j in range(len(tasks)):
#             condition_unit.append(tasks[j])
#             for k in range(len(careers)):
#                 condition_unit.append(careers[k])
#                 for u in range(len(foods)):
#                     condition_unit.append(foods[u])
#                     conditions["".join(condition_unit)] = []  # 이 리스트에는 조건에 맞는 점수들이 담긴다
#
#     # info를 파싱하여 key를 구하고 value list 들에 값을 채운다
#     # info는 무조건 다섯덩어리로 들어온다
#     # ex : "java backend junior pizza 150"
#     for data in info:
#         data_list = data.split()
#         key = "".join(data_list[:4])  # 이렇게 할 수 있는 거 맞나..?
#         conditions[key].append(int(data_list[4]))  # 점수 추가
#
#         # ※※※※※※※※※
#         # 하나의 데이터가 여러 key에 해당될 수도 있는데..? 이걸 어떻게 구현?
#         # 지금은 하나의 key에만 값이 할당됨
#         # ex : "java backend junior pizza"는 "java", "java backend" 두 조건에 동시에 해당될 수 있음
#         # ※※※※※※※※※
#
#     # 이진탐색을 위해 value list 들을 정렬
#     for key in conditions.keys():
#         conditions[key].sort()
#
#     # 이제 이진탐색을 하기 위해 또 query를 파싱해야 한다
#     # and를 기준으로 자르고 "-"를 ""로 replace
#     # ex : "cpp and - and senior and pizza 250"
#     # 이거 어케 짜름..?
#     for q in query:
#         query_list = q.split(" and ")  # 마지막 원소는 "소울푸드+점수" 라서 한 번 더 잘라야 한다
#
#         # query_list[3] == "pizza 250"
#         key = query_list[:3] + query_list[3].split()[0].replace("-", "")
#         score = query_list[3].split()[1]  # 점수만 뺴내기
#
#         list_size = len(conditions[key])
#         left_idx = bisect_left(conditions[key], score)
#         answer.append(list_size - left_idx)
#
#     return answer
#
#
# if __name__ == '__main__':
#     solution()


from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []
    condition_dict = {}

    for data in info:
        data_list = data.split()
        key_list = data_list[:-1]
        score = int(data_list[-1])

        for i in range(5):
            for comb in combinations(key_list, i):
                key = "".join(comb)
                if key in condition_dict:
                    condition_dict[key].append(score)
                else:
                    condition_dict[key] = [score]

    # 이진 탐색을 위한 정렬
    for key in condition_dict.keys():
        soso_list = condition_dict[key]
        soso_list.sort()

    for q in query:
        query_list = q.split(" and ")
        key = ("".join(query_list[:-1]) + query_list[-1].split()[0]).replace("-", "")
        score = int(query_list[-1].split()[1])  # 점수만 뺴내기

        if key in condition_dict:
            list_size = len(condition_dict[key])
            left_idx = bisect_left(condition_dict[key], score)
            answer.append(list_size - left_idx)
        else:
            answer.append(0)

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