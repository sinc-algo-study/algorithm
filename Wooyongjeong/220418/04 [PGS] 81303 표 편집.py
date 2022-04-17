"""
N이 100만

배열을 사용하면.. 최악의 경우 U, D, C 명령이 O(N)만큼 걸림
링크드 리스트 -> U, D는 움직이는 만큼 O(X)일거고, C 명령 O(1)만에 가능
"""


from typing import List, Dict


def delete(cur: int, answer: List[str],
           ll: Dict[int, List[int]], stack: List[List[str]]) -> int:
    # 삭제
    answer[cur] = 'X'
    prev, next = ll[cur]
    stack.append([prev, cur, next])

    if prev == None:
        # cur이 첫 행인 경우
        ll[next][0] = None
    elif next == None:
        # cur이 마지막 행인 경우
        ll[prev][1] = None
    else:
        ll[prev][1] = next
        ll[next][0] = prev

    # 지운 게 마지막 행이라면 바로 이전 행을 선택해야 함
    # 아니라면 그 다음 행
    return ll[cur][0] if next == None else ll[cur][1]


def undo(answer: List[str],
           ll: Dict[int, List[int]], stack: List[List[str]]) -> None:
    # 되돌리기
    prev, now, next = stack.pop()
    answer[now] = 'O'

    if next == None:
        # 되돌릴 행이 마지막 행이었던 경우
        ll[prev][1] = now
    elif prev == None:
        # 되돌릴 행이 첫 행이었던 경우
        ll[next][0] = now
    else:
        ll[next][0] = now
        ll[prev][1] = now


def move(cur: int, c: List[str], ll: Dict[int, List[int]]) -> int:
    # 위로 이동 or 아래로 이동
    prev_or_next = 0 if c[0] == 'U' else 1
    x = int(c[1])
    for _ in range(x):
        cur = ll[cur][prev_or_next]
    return cur


def solution(n: int, k: int, cmd: List[str]) -> str:
    answer = ['O'] * n
    # doubly linked-list를 dict로 표현
    ll = {i: [i - 1, i + 1] for i in range(n)}
    ll[0] = [None, 1]
    ll[n - 1] = [n - 2, None]

    cur = k  # 현재 위치
    stack = []  # 'Z' 명령을 위한 스택

    for c in cmd:
        c = c.split()
        if c[0] == 'C':
            # 삭제
            cur = delete(cur, answer, ll, stack)
        elif c[0] == 'Z':
            # 되돌리기
            undo(answer, ll, stack)
        else:
            # 위 or 아래
            cur = move(cur, c, ll)

    return ''.join(answer)
