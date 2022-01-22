'''

s의 절반 길이까지만 검사하면 된다.
그 이상의 단위로 자르는 건 압축 자체가 불가하므로 무의미

브루트포스 가능한가?
1. s 최대 길이 1000
2. 1~500 전부 검사하려면 시간이 얼마나 필요한가?
-> 대략 500 * 1000 * 1000
-> 자르는 단위 * 체크 대상 문자열 길이 * 단위가 포함됐는지 확인할 문자열 길이
-> 약 500,000,000..... 5*10^8....?

프로그래머스는 10초니까 돌아가긴 할 거 같긴 한데...
시간복잡도 이게 맞나..?


500 * 1000


'''


def solution(s):
    answer = 1001
    if len(s) == 1:  # 예외처리 필수
        return 1

    # 500
    for i in range(1, len(s)//2 + 1):  # 절반만 체크
        p = 0  # 현재 좌표 (position)
        length = len(s)

        # 1000
        while p+i <= len(s):  # 압축 가능 여부 확인 가능한 길이가 남아있는가?
            sub = s[p:p+i]  # JAVA.String.substring() 대신 슬라이싱 사용 가능
            p += i  # 압축이 불가하더라도 포지션은 이동해야한다

            # 1000
            cnt = 0  # 압축 횟수
            while p+i <= len(s):  # 압축 가능 여부 확인 가능한 길이가 남아있는가?
                if sub == s[p:p+i]:
                    cnt += 1
                    p += i
                else:  # 더이상 압축이 불가하면 새로운 sub를 찾는다
                    break

            if cnt > 0:
                length -= cnt*i
                length += len(str(cnt+1))  # 반복 횟수의 길이 더한다. 최초의 sub는 cnt에 포함되지 않기 때문에 cnt+1 해줘야함

        answer = min(answer, length)

    return answer


if __name__ == '__main__':
    ss = [
        "aabbaccc",  # 7
        "ababcdcdababcdcd",  # 9
        "abcabcdede",  # 8
        "abcabcabcabcdededededede",  # 14
        "xababcdcdababcdcd"  # 17
    ]

    for s in ss:
        print("s =", s + ", result =", solution(s))




