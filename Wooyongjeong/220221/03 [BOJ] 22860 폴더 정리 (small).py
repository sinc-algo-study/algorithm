from enum import Enum
import collections
import sys
sys.setrecursionlimit(10**6)


class Type(Enum):
    FILE = 0
    FOLDER = 1


def solution(N, M, Q, file_infos, queries):
    def search_file_system(now, files):
        for f, c in file_system[now]:
            if c == Type.FILE.value:
                files.append(f)
            elif c == Type.FOLDER.value:
                search_file_system(f, files)

    file_system = collections.defaultdict(list)
    for info in file_infos:
        p, f, c = info.split()  # 상위 폴더 p, 폴더 또는 파일 f, 폴더 플래그 c
        file_system[p].append([f, int(c)])
    print(file_system)

    for query in queries:
        query = query.split('/')
        files = []
        search_file_system(query[-1], files)
        print(len(set(files)), len(files))


if __name__ == '__main__':
    N, M = map(int, input().split())
    file_infos = [input() for _ in range(N + M)]
    Q = int(input())
    queries = [input() for _ in range(Q)]
    solution(N, M, Q, file_infos, queries)
