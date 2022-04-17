"""
1. 괄호로 묶지 않고 바로 다음 숫자와 연산
2. 괄호로 묶고 다음 숫자와 다다음 숫자를 연산한 결과와의 연산

1번, 2번을 재귀함수로 풀면 될 듯

수는 0~9, 연산자는 +,-,*
"""


def dfs(idx: int, value: int) -> None:
    if idx >= N:
        global ans
        ans = max(ans, value)
        return

    operation = '+' if idx == 0 else exp[idx - 1]
    if idx + 2 < N:
        # 괄호로 묶기
        dfs(idx + 4, eval(f"{value}{operation}({exp[idx: idx + 2 + 1]})"))
    # 괄호로 묶지 않기
    dfs(idx + 2, eval(f"{value}{operation}{exp[idx]}"))


if __name__ == '__main__':
    N = int(input())
    exp = input()
    ans = float('-inf')
    dfs(0, 0)
    print(ans)
