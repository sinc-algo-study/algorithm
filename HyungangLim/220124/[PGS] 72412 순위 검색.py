'''

조건을 만족하는 사람 중 X점 이상인 사람
조건 기준
1. 언어 j c p -
2. 직군 b f -
3. 경력 j s -
4. 푸드 c p -
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
-> 1~4 조건의 모든 경우의 수의 key를 생성. 각 조건에 해당하는 value는 점수값을 담는 리스트로 하자. [점수, 점수, 점수  .... ]

일단 조건에 대해 keySet을 만들어야 함
-> 4 * 3 * 3 * 3 = 108개의 key 존재 (아무것도 안 고르는 경우도 존재한다)


아!! value값인 list를 오름차순 정렬하고 이진탐색으로 해당 점수를 빠르게 구하면 됨!!
hashmap으로 한 번 줄이고, 이진탐색으로 또 한 번 줄이고

'''


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
