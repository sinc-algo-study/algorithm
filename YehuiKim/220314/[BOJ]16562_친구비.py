import sys
input = sys.stdin.readline

'''
그래프! 유니온파인드!
관계 연결해서, 각 사이클의 친구비 제일 적은 값 합친 cost 도출
cost가 k보다 적으면 cost 출력, 넘치면 Oh no 출력

=> 주의!!
노드 간의 연결은 되었으나, parent 리스트에서 하나의 부모노드로 전체가
한번에 업뎃 안되는 문제 발생
[반례]
5 4 100
1 1 1 1 1
1 5
2 4
4 3
5 4
=>답 : 1
'''

def find(x):
    if x==parent[x]:
        return x
    else:
        return parent[x]


def notRoot(x):
    if x not in notRoots:
        notRoots.add(x)


def union(a, b):
    a = find(a)
    b = find(b)
    # 비용이 적은 노드가 루트 되도록
    if fee[a] > fee[b]:
        prnt, child = b, a
    # 비용이 같으면 더 적은 숫자가 루트 되도록
    elif fee[a] == fee[b]:
        if a>b:
            prnt, child = b, a
        else:
            prnt, child = a, b
    else:
        prnt, child = a, b
    parent[child]=prnt
    # 부모노드에서 자식노드가 된 노드를 따로 저장해둠 (추후 비용 계산시 제외하기 위해)
    notRoot(child)


if "__main__" == __name__:
    n, m, k = map(int, input().split())
    fee = [0]+list(map(int, input().split()))
    parent = [i for i in range(n+1)]
    notRoots = set()
    for _ in range(m):
        a, b = map(int, input().split())
        union(a, b)

    cost = sum([fee[i] for i in set(parent) if i not in notRoots])
    if cost<=k:
        print(cost)
    else:
        print("Oh no")
    print(parent)