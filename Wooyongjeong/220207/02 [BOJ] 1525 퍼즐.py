import collections


def swap(x, y, nx, ny, table):
    # python에서 str 변수는 immutable이기 때문에
    # list로 변환하여 swap하고 str로 다시 만들어 반환하여 사용
    temp = list(table)
    temp[x * 3 + y], temp[nx * 3 + ny] = temp[nx * 3 + ny], temp[x * 3 + y]
    return ''.join(temp)


def solution(table):
    dest = '123456780'
    q = collections.deque()
    q.append((table[:], 0))
    visited = collections.defaultdict(bool)

    while q:
        now, cnt = q.popleft()
        if now == dest:
            return cnt

        # table에서 '0'의 위치 zero를
        # 3으로 나눈 몫은 테이블에서의 행 번호, 나머지는 열 번호
        zero = now.find('0')
        x = zero // 3
        y = zero % 3

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 3 and 0 <= ny < 3:
                now = swap(x, y, nx, ny, now)
                if not visited[now]:
                    visited[now] = True
                    q.append((now[:], cnt + 1))
                now = swap(x, y, nx, ny, now)
    return -1


if __name__ == '__main__':
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    table = [input().split() for _ in range(3)]
    table = ''.join(''.join(t) for t in table)
    print(solution(table))
