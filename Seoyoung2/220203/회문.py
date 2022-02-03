from sys import stdin
'''
- 회문이면 0, 유사 회문이면 1, 둘 모두 아니면 2

1 ≤ T ≤ 30, 주어지는 문자열의 길이는 3 이상 100,000 이하

틀린 풀이) 양끝에서 비교하다가 다른 글자가 나오면 왼쪽->오른쪽 순으로 체크
     axaaxaa 이런 예시에서 틀릴 수 있음

'''

T = int(stdin.readline())
for _ in range(T):
    x = stdin.readline().strip()
    if x == x[::-1]:
        print(0)
    else:
        left, right = 0, len(x)-1
        while left < right:
            if x[left] == x[right]:
                left += 1
                right -= 1
            else:
                # 다른 알파벳을 마주한 인덱스 : left, right
                break
        xl = x[:left] + x[left+1:]
        xr = x[:right] + x[right+1:]
        print(1 if xl == xl[::-1] or xr == xr[::-1] else 2)