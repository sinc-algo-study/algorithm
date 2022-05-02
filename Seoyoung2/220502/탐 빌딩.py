N = int(input())
power = list(map(int, input().split()))

# 간격은 줄어드니까 힘의 최솟값을 키워야함
i, j = 0, N-1
ans = 0
while i < j:
    tmp = (j-i-1) * min(power[i], power[j])
    ans = max(ans, tmp)
    if power[i] < power[j]:
        i += 1
    else:
        j -= 1
print(ans)