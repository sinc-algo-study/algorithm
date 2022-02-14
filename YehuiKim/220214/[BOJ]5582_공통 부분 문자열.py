import sys
input = sys.stdin.readline


# 1~4000
# 4000 2000 1333 1000 800 666 577 500 444 400
# for문 이용한 단순 비교 => 시간 초과
def common_words(short, long):
    if short == long:
        return len(short)
    s_len = len(short)
    l_len = len(long)
    # short한 문자 기준으로 s_len -> 1만큼 길이를 가져와서 비교
    for l in range(s_len, 0, -1): # 11, 10, ..., 1
        for sl in range(s_len - l +1): # 11-11+1(0) / 11-10+1(0,1) /
            sub_s = short[0+sl:l+sl] # 0+0:11+0 / 0+0:10+0, 0+1:10+1 /
            for ll in range(l_len - l): # 16-11 = 5 => 0,1,...,5
                sub_l = long[0+ll:l+ll] # 0+0:11+0, 0+1:11+1, ...
                if sub_s == sub_l:
                    return l
    return 0


# 이게 찐
def dp(a, b):
    n = len(a)
    m = len(b)
    maxi = 0
    memo = [0 for _ in range(m+1)]
    for i in range(1, n+1):
        tmp_memo = [0 for _ in range(m + 1)]
        for j in range(1, m+1):
            if a[i-1]==b[j-1]:
                tmp_memo[j] = memo[j-1]+1
                maxi = max(maxi, tmp_memo[j])
        memo = tmp_memo
    return maxi


if '__main__' == __name__ :
    a = list(input().rstrip())
    b = list(input().rstrip())
    print(dp(a, b))




