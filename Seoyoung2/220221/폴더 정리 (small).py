import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
'''
tree 만들어서? dictionary 가능? parent 배열 따라가게?

*** 파일 이름이 같을 수가 있음 (파일만, 폴더는 아님) => dictionary ㄱㄱ
'''
N, M = map(int, sys.stdin.readline().split())

com = defaultdict(list)
for _ in range(N+M):
    P, F, C = sys.stdin.readline().split()  # 상위폴더/이름/1(폴더)0(파일)
    com[P].append((F, C))
# {'main': [('FolderA', '1'), ('FolderB', '1')]
# , 'FolderA': [('File1', '0'), ('File2', '0')]
# , 'FolderB': [('FolderC', '1'), ('File1', '0'), ('File3', '0')]})


def search_file(parent):
    for child, flag in com[parent]:
        if flag == '1':
            search_file(child)
        else:
            files.append(child)


Q = int(sys.stdin.readline())
for _ in range(Q):
    qs = sys.stdin.readline().strip().split("/")
    files = []
    search_file(qs[-1])
    print(len(set(files)), len(files))
