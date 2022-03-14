import sys
input = sys.stdin.readline

'''
<목표 : 연속된 부분합의 최대 구하기>
- 연속된 부분이 끊기는 기준 : 이전 값들의 합+현재값 vs 현재값 => 현재값이 더 크면 끊기
    => 현재값이 더 크므로, 더했을 때 합계를 오히려 감소시키는 "이전의 값들의 합"은 
        어차피 의미가 없다. 그래서 새로 시작해도 무방
=> subMaxDP : 제외 없는 최댓값

- 제외할 수 결정 기준 : 이전값들의 합 (현재값 제외) 
        vs 이미제외시킨 이전값들의 합(이전값 전체의 합 말하는거 아니고 이전 원소에 기록한 최대치)
=> exceptSubMaxDP : 이 리스트에는 해당 위치값 제외시킨 합의 매 상황 최대값만 담아줌
'''

def main():
    subMaxDP[0]=arr[0]
    exceptSubMaxDP[0]=0
    answer = arr[0]
    for i in range(1, n):
        subMaxDP[i]=max(subMaxDP[i-1]+arr[i],arr[i])
        exceptSubMaxDP[i]=max(subMaxDP[i-1],exceptSubMaxDP[i-1]+arr[i])
        answer = max(subMaxDP[i],exceptSubMaxDP[i], answer)
    return answer


if "__main__" == __name__:
    n = int(input().rstrip())
    arr = list(map(int, input().split()))
    subMaxDP = [0 for _ in range(n)]
    exceptSubMaxDP = [0 for _ in range(n)]
    print(main())

