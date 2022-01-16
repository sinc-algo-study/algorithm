# - board에 담겨있는 형태는, 가로줄 윗줄부터 차례대로 담긴다
# - 해당칸이 0일 수 있다(세로줄 전체도) ⇒ 0인지 체크하고 pass하도록
# - basket의 맨 마지막 요소가 이번에 넣는 요소와 같은지 확인 ⇒ 같으면 둘다 삭제

def solution(board, moves):
    basket = []
    ans = 0
    for i in moves:
        for j in range(len(board)):
            tmp = 0
            if(board[j][i-1]!=0):
                tmp, board[j][i-1] = board[j][i-1], 0
                break
        if tmp !=0:
            if not basket:
                basket.append(tmp)
            else:
                b_tmp = basket.pop()
                if b_tmp == tmp:
                    ans += 2
                else :
                    basket.append(b_tmp)
                    basket.append(tmp)
    return ans