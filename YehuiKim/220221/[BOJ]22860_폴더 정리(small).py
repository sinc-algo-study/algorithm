import sys
input = sys.stdin.readline
from collections import deque

'''
1. 구조 잡기
이중(?) 딕셔너리 구조
=> drive = {main:{0:[~], 1:[~]}, folderA:{0:[~], 1:[~], ...}
    => 0이면 key 0에 저장, 1이면 key 1에 저장

2. 주어진 경로에 대한 파일 종류수, 파일 수 출력하기 위해 큐 사용
=> 큐에 폴더 넣고, 해당 폴더 안의 요소들을 따져줄 것임
=> 경로의 맨 마지막 폴더명인 요소를 큐에 추가
    ex) main/FolderA면 키가 FolderA인 원소 가져옴 (앞의 경로는 신경 쓸 필요x)
=> 큐에서 폴더 하나씩 꺼내서, 해당 폴더 안에 폴더가 또 있으면 큐에 넣고, 파일이면 카운트 해줌.
    => 종류를 세기 위해 파일도 리스트 안에 저장함. 이미 리스트에 있으면, 파일 수만 +1 파일 종류수는 그대로 

(실수)
입력 실수함
- 텍스트에만 rstrip걸어줘야 하는데, int값에도 rstrip걸어줌
'''
if '__main__' == __name__ :
    n, m = map(int, input().split())

    drive = dict()
    for _ in range(n+m):
        temp = input().split()
        fold_a = temp[0]
        fold_b = temp[1]
        yn = temp[2]
        if fold_a in drive.keys(): # 기존에 있으면
            tmp = drive[fold_a] # 키(fold_a)에 대한 딕셔너리 가져오기
            ttmp = tmp[yn] # 키(yn)에 대한 리스트 가져오기
            ttmp.append(fold_b) # 원소를 리스트에 추가
            tmp[yn] = ttmp # 추가한 신규 리스트로 대체
        else: # 기존에 없으면
            tmp = {'0':[], '1':[]}
            tmp[yn].append(fold_b)
            drive[fold_a] = tmp
    case_n = int(input())
    answer = []
    for k in range(case_n):
        temp = input().rstrip().split('/')
        cnt = 0
        files = []
        que = deque()
        que.append(temp[-1])
        while que:
            #print(que)
            now = que.pop()
            if now not in drive.keys():
                continue
            for i in drive[now].keys():
                if i=='1': # 1(폴더)이면
                    for j in drive[now][i]:
                        que.append(j)
                else: # 파일이면
                    #print(drive[now][i])
                    for j in drive[now][i]:
                        cnt += 1
                        if j not in files:
                            files.append(j)
        answer.append((len(files), cnt))

    for i,j in answer:
        print(i, j)

