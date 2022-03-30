import collections


def kill_trees(x, y, trees, idx, board):
    for i in range(idx, len(trees)):
        board[x][y] += trees[i] // 2
    for _ in range(len(trees) - idx):
        trees.pop()


def spring_and_summer(board, tree_info):
    for loc, trees in tree_info.items():
        x, y = loc

        for i, age in enumerate(trees):
            if board[x][y] >= age:
                board[x][y] -= age
                trees[i] += 1
            else:
                kill_trees(x, y, trees, i, board)
                break


def breed_trees(n, x, y, tree_info):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nx = x + i
            ny = y + j
            if 0 <= nx < n and 0 <= ny < n:
                tree_info[(nx, ny)].appendleft(1)


def fall(n, tree_info):
    for loc, trees in list(tree_info.items()):
        x, y = loc
        grown_tree_cnt = len(list(filter(lambda t: t % 5 == 0, trees)))
        for _ in range(grown_tree_cnt):
            breed_trees(n, x, y, tree_info)


def winter(n, board, nutrients):
    for i in range(n):
        for j in range(n):
            board[i][j] += nutrients[i][j]


def get_tree_cnt(tree_info):
    cnt = 0
    for trees in tree_info.values():
        cnt += len(trees)
    return cnt


def solution(n, k, nutrients, trees):
    board = [[5] * n for _ in range(n)]
    # [행, 열, 나이]
    tree_info = collections.defaultdict(collections.deque)
    for x, y, z in trees:
        tree_info[(x - 1, y - 1)].append(z)

    for _ in range(k):
        spring_and_summer(board, tree_info)
        fall(n, tree_info)
        winter(n, board, nutrients)

    return get_tree_cnt(tree_info)


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    nutrients = [list(map(int, input().split())) for _ in range(N)]
    trees = [list(map(int, input().split())) for _ in range(M)]
    print(solution(N, K, nutrients, trees))
