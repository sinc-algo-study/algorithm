
def solution(board, moves):
    answer = 0
    stk = []

    for m in moves:
        col = m - 1
        for b in board:
            # 열은 고정. 행만 이동하며 인형 체크
            if b[col] != 0:  # 인형 찾음
                if len(stk) == 0:
                    stk.append(b[col])
                    b[col] = 0
                else:
                    if b[col] == stk[-1]:
                        answer += 2
                        b[col] = 0
                        stk.pop()
                    else:
                        stk.append(b[col])
                        b[col] = 0
                break
    return answer



if __name__ == '__main__':
    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2],
             [3, 5, 1, 3, 1]]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]
    print(solution(board, moves))