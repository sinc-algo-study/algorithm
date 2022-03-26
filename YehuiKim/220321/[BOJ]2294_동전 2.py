import sys
input = sys.stdin.readline


if "__main__"==__name__:
    # 아래처럼 하면, 중간의 동전을 건너뛸 수 없는 문제 발생
    '''
    n, k = map(int, input().split())
    coins = set()
    for _ in range(n):
        coins.add(int(input()))
    coins = sorted(coins, reverse=True)
    ans = 1000000001
    n = len(coins)
    for i in range(n):
        temp = k
        cnt = 0
        j = i
        while temp > 0:
            if j >= n:
                cnt = 1000000001
                break
            cnt += temp//coins[j]
            temp %= coins[j]
            j += 1
        #print(cnt)
        ans = min(ans, cnt)
    if ans == 1000000001 : ans = -1
    print(ans)
    '''
    # 아래처럼 dp에 저장하는 식으로 해야지 중간의 동전을 건너뛸 수 있음
    # 주의 : k는 10000 이하이지만, 동전의 값은 100000 이하므로, 동전이 k보다 큰 값이면 건너뛰도록 해야함
    n, k = map(int, input().split())
    coins = set()
    for _ in range(n):
        coins.add(int(input()))
    coins = sorted(coins)
    n = len(coins)
    dp = [10001]*(k+1)
    for i in range(n):
        if coins[i]<=k:
            dp[coins[i]]=1
            for j in range(coins[i],k+1):
                dp[j]=min(dp[j], dp[j-coins[i]]+1)
    if dp[-1]==10001: dp[-1]=-1
    print(dp[-1])
