def dfs(now, money):
    global arrival

    if arrival:
        return

    room_kind, cost = rooms[now]
    if room_kind == 'L':
        if money < cost:
            money = cost
    elif room_kind == 'T':
        money -= cost

    if money < 0:
        return

    if now == n:
        arrival = True
        return

    for next_room in graph[now]:
        if visited[next_room]:
            continue
        visited[next_room] = True
        dfs(next_room, money)
        visited[next_room] = False


while True:
    n = int(input())
    if n == 0:
        break
    rooms = [None]
    graph = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    for i in range(1, n + 1):
        room = input().split()
        rooms.append((room[0], int(room[1])))

        for next_room in room[2:-1]:
            graph[i].append(int(next_room))

    arrival = False
    start, money = 1, 0
    visited[start] = True
    dfs(start, money)
    print("Yes" if arrival else "No")
