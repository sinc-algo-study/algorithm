import sys
input = sys.stdin.readline

'''
핵심 : 규칙을 찾아서, 작은 것부터 큰 것을 해결해나가는 DP 
=> 주어진 문제도 작은 케이스의 최댓값이 큰 케이스에 적용되기 때문에 DP임
관건 : 횟수가 최대 2번이므로, n번째 일때 가능한 케이스는 아래와 같다. (n>3)
    먹 먹 X
    먹 X 먹
    먹 X X
    X 먹 먹
    X 먹 X
    (X X 먹 이나 X X X는 어차피 안먹으면 횟수 초기화되기 때문에 고려안한다)
1) 저번 두 번을 먹었다면, 이번에 먹지 못하는 것은 당연하다
    먹 먹 X
2) 하지만 저번에 먹지 않았다고, 이번에 꼭 먹어야 하는 것은 아니다.
    먹 X 먹
    먹 X X
    X 먹 먹
    X 먹 X
 => 이번에 먹지 않으면 먹은 횟수가 초기화되므로, 
    이번에 먹지 않은 것들 중에서, 먹은양이 최대인 것만 남긴다.
    먹 X 먹
    X 먹 먹
    max(? ? X) (전에 먹든 안먹든 지금 안먹었기 때문에 초기화돼서 노상관)
 => 매 횟수에서 위 세 가지 케이스만 고려하면 된다!

7
100
100
1
1
1
100
100
=> 401

# 4번째
201
o o x  o
200
o o x  x
102
o x o  o
101
o x o  x 
101
x o o  x

=> 5번째
202
o o x o o
201
o o x x o
201
o o x o x

=> 6번째
202
o o x o o x
301
o o x x o o
301
o o x o x o

=> 7번째
302
o o x o o x o
301
o o x x o o x
401
o o x o x o o
'''

def drinking(wines):
    length = len(wines)
    if length==1:
        return wines[0]
    elif length==2:
        return sum(wines)
    else:
        dp = []
        dp.append(wines[0])
        dp.append([wines[0]+wines[1], wines[0], wines[1]])
        for i in range(2, length):
            temp = []
            if (i % 3) == 2:  # 3의 배수
                temp.append(max(dp[i-1]))
                temp.append(dp[i-1][1]+wines[i])
                temp.append(dp[i-1][2]+wines[i])
                dp.append(temp)
            elif (i % 3) == 0:  # 3의 배수+1
                temp.append(dp[i - 1][0] + wines[i])
                temp.append(dp[i - 1][1] + wines[i])
                temp.append(max(dp[i-1]))
                dp.append(temp)
            else:  # 3의 배수+2
                temp.append(dp[i - 1][0] + wines[i])
                temp.append(max(dp[i-1]))
                temp.append(dp[i - 1][2] + wines[i])
                dp.append(temp)
        return max(dp[length-1])


if '__main__' == __name__:
    n = int(input().rstrip())
    wines = [int(input().rstrip()) for _ in range(n)]
    print(drinking(wines))