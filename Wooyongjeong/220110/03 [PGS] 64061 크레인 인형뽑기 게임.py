from collections import deque


def solution(board, moves):
    n = len(board)
    basket = deque()  # 바구니
    stacks = [deque() for _ in range(n + 1)]  # board의 각 열 stack
    for j in range(n):
        for i in range(n - 1, -1, -1):
            if board[i][j] == 0:
                break
            stacks[j + 1].append(board[i][j])

    popped_dolls = 0
    for move in moves:
        if not stacks[move]:
            # 해당 위치에 인형이 없다면 continue
            continue
        doll = stacks[move].pop()  # 해당 열 제일 위에 있는(peek) 인형 pop
        if basket and basket[-1] == doll:
            # 바구니 제일 위(peek)이 같은 인형이라면 터뜨림
            popped_dolls += 2
            basket.pop()
            continue
        # 아니면 그냥 넣기
        basket.append(doll)

    return popped_dolls


if __name__ == '__main__':
    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2],
             [3, 5, 1, 3, 1]]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]
    print(solution(board, moves))
