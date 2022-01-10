# 2019 카카오 개발자 겨울 인턴십

def solution(board, moves):
    tmp = []
    ans = 0
    for m in moves:
        for b in board:
            if b[m-1] != 0:
                if b[m-1] == tmp[-1]:
                    ans += 2
                    tmp.pop()
                else:
                    tmp.append(b[m-1])
                b[m-1] = 0
                break
    return ans


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))   #4

