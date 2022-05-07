"""
N <= 10만

NC2 = 대충 49억으로 시간 초과 날거임
O(N)이나 O(NlogN)정도로 풀어야함

팀 능력치: (a와 b 사이에 존재하는 사람 수) * min(a 능력치, b 능력치)
-> a 능력치와 b 능력치 중 누가 더 작은지 확인
-> a 능력치가 더 작다면 b를 왼쪽으로 이동시켜봤자 최소 능력치는 a 능력치임
    -> 그럼 a를 오른쪽으로 늘려야겠네
"""


def get_team_ability(i: int, j: int, status: list[int]) -> int:
    return (j - i - 1) * min(status[i], status[j])


def solution(n: int, status: list[int]) -> int:
    start, end = 0, n - 1
    ans = get_team_ability(start, end, status)

    while start <= end:
        if status[start] < status[end]:
            start += 1
        else:
            end -= 1

        ability = get_team_ability(start, end, status)
        ans = max(ans, ability)

    return ans


if __name__ == '__main__':
    N = int(input())
    status = list(map(int, input().split()))
    print(solution(N, status))
