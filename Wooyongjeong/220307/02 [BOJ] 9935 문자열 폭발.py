def solution(s, bomb):
    stack = []
    for c in s:
        stack.append(c)
        if c == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
            # 슬라이싱을 이용하여 stack의 tail에서 bomb 크기만큼 삭제
            del stack[-len(bomb):]
            '''
            # bomb 크기만큼 stack에서 pop
            for _ in range(len(bomb)):
                stack.pop()
            '''

    answer = ''.join(stack)
    return answer if answer != '' else 'FRULA'


if __name__ == '__main__':
    s = input()
    bomb = input()
    print(solution(s, bomb))
