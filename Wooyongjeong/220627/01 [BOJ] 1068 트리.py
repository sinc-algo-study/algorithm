DELETED = -2
n = int(input())
arr = list(map(int, input().split()))
delete_node = int(input())

ans = 0


def delete(now):
    arr[now] = DELETED
    for i in range(n):
        if now == arr[i]:
            delete(i)


delete(delete_node)
for i in range(n):
    if arr[i] != DELETED and i not in arr:
        # 지워진 트리는 DELETED 표시를 했고,
        # arr에는 부모 노드들, 즉 리프 노드가 아닌 노드들이 있으므로
        # i가 arr에 없다면 리프 노드임
        ans += 1
print(ans)
