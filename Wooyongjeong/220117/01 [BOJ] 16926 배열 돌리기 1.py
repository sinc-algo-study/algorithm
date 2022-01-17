if __name__ == '__main__':
    N, M, R = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for _ in range(R):
        rotate_count = min(N, M) // 2

        # 각 사각형을 돌릴 때마다 기준점은 (0, 0), (1, 1), ...
        for start in range(rotate_count):
            # 이번 돌릴 차례의 가장 큰 x값
            x_max = N - start - 1
            # 이번 돌릴 차례의 가장 큰 y값
            y_max = M - start - 1

            tmp = arr[start][start]  # 돌리기 전에 가지고 있어야 함
            for j in range(start, y_max):
                # 위쪽 변. x: 고정, y: ←
                arr[start][j] = arr[start][j + 1]
            for i in range(start, x_max):
                # 오른쪽 변. x: ↑, y: 고정
                arr[i][y_max] = arr[i + 1][y_max]
            for j in range(y_max, start, -1):
                # 아래쪽 변. x: 고정, y: →
                arr[x_max][j] = arr[x_max][j - 1]
            for i in range(x_max, start, -1):
                # 왼쪽 변. x: ↓, y: 고정
                arr[i][start] = arr[i - 1][start]

            arr[start + 1][start] = tmp  # 마지막에 시작지점 값도 돌림

    for a in arr:
        print(*a)
