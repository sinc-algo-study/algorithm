import collections
from typing import List, DefaultDict


def find_every_possible_str(board: List[List[str]]) -> DefaultDict[str, int]:
    """
    board에서 찾을 수 있는 모든 길이가 1 이상 5 이하인 문자열의 개수를 세보는 함수
    """
    def dfs(x: int, y: int, now: str) -> None:
        find[now] += 1

        if len(now) == 5:
            # 신이 좋아하는 문자열의 최대 길이는 5
            return

        for dx, dy in zip(dxs, dys):
            # 격자가 환형으로 이어짐
            nx = (x + dx + N) % N
            ny = (y + dy + M) % M
            dfs(nx, ny, now + board[nx][ny])

    find = collections.defaultdict(int)  # {문자열: 개수}

    for i in range(N):
        for j in range(M):
            # 모든 칸에서 시작해봄
            dfs(i, j, board[i][j])

    return find


def solution(board: List[List[str]], strs: List[str]) -> None:
    find = find_every_possible_str(board)

    for s in strs:
        print(find[s])


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    strs = [input() for _ in range(K)]
    dxs = [1, 1, 1, 0, 0, -1, -1, -1]
    dys = [1, 0, -1, 1, -1, 1, 0, -1]
    solution(board, strs)
