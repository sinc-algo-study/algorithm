'''

그냥 회문만 검사하면 슬라이싱을 사용한 브루트포스도 가능
여기선 유사회문 검사때문에 브루트 포스 불가

투 포인터 사용하여 하나씩 비교하며 판별
-> 반례 발생

(반례)
input :
1
baaba
output :
2
answer :
1


양방향으로 검사 싨시 -> 왼쪽부터 검사, 오른쪽부터 검사
30 * 100,000 * 2 = 6,000,000
-> 가능

질문 1. left, right 따로 호출하지 않고 하나의 while에서 left, right 동시에 처리 가능할지?
질문 2. 가능하다면 기존 방식과 시간복잡도가 달라질까?

'''


# def solution(target):
#     cnt = 0  # 제외한 문자 수
#     left, right = 0, len(target) - 1
#
#     while left <= right:
#         if target[left] == target[right]:
#             left += 1
#             right -= 1
#         else:
#             if cnt == 1:
#                 return 2
#
#             # 어느 쪽 문자를 지울 것인지 결정해야함
#             cnt += 1
#             if target[left + 1] == target[right]:
#                 left += 1
#             elif target[left] == target[right - 1]:
#                 right -= 1
#             else:  # 두 번 지워도 불가능
#                 return 2
#
#     return 0 if cnt == 0 else 1


def check_palin(target, d):
    # dir : 0 = left, 1 = right

    cnt = 0
    left, right = 0, len(target) - 1
    while left <= right:
        if target[left] == target[right]:
            left += 1
            right -= 1
        else:
            if cnt == 1:
                return 2

            cnt += 1
            if d:  # left first
                if target[left + 1] == target[right]:
                    left += 1
                elif target[left] == target[right - 1]:
                    right -= 1
                else:  # 두 번 지워도 불가능
                    return 2

            else:  # right first
                if target[left] == target[right - 1]:
                    right -= 1
                elif target[left + 1] == target[right]:
                    left += 1
                else:
                    return 2

    return cnt


def solution(target):
    left_cnt = check_palin(target, 0)
    right_cnt = check_palin(target, 1)

    return 0 if left_cnt == 0 or right_cnt == 0 else \
        1 if left_cnt == 1 or right_cnt == 1 else 2


if __name__ == '__main__':
    T = int(input())
    str_list = [input() for _ in range(T)]

    for i in str_list:
        print(solution(i))

