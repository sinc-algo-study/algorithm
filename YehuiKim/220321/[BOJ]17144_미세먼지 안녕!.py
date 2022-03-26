import sys
input = sys.stdin.readline
'''
공청기 좌표 표시해두기
t번 돌기
1. -1도 0도 아니면 미세먼지이면, 미세먼지 확산
    각 칸//5 씩 4방향으로 새 리스트에 담아주기
    단 공청기 있거나, 영역 밖이면 무시 => 확산된 칸 카운트
    기존 리스트에는 기존-확산된양만 남기기
2. 기존 리스트 += 새 리스트
3. 공청기 작동
    위쪽 좌표 : 반시계
    => (x는 한칸씩 오른쪽,y동일),(x=c,y는 한칸씩 위로),
        (x는 한칸씩 왼쪽,y=0),(x=0,y는 한칸씩 아래로)
    아래쪽 좌표 : 시계
    => (x는 한칸씩 오른쪽,y동일),(x=c,y는 한칸씩 아래로),
        (x는 한칸씩 왼쪽,y=r),(x=0,y는 한칸씩 위로)
4. 전체 리스트의 합 +2(공청기-1값 두개 상쇄)를 return
'''
def operateCleaner():
    ar1 = cleaner[0]
    for i in range(ar1-1, 0, -1):
        room[i][0]=room[i-1][0]
    room[0][:CC-1]=room[0][1:]
    for i in range(ar1):
        room[i][CC-1]=room[i+1][CC-1]
    room[ar1][1:] = [0]+room[ar1][1:CC-1]

    ar2 = cleaner[1]
    for i in range(ar2+2, RR):
        room[i-1][0]=room[i][0]
    room[RR-1][:CC-1]=room[RR-1][1:]
    for i in range(RR-2, ar2-1, -1):
        room[i+1][CC-1]=room[i][CC-1]
    room[ar2][1:] = [0]+room[ar2][1:CC-1]


def dustMove(room):
    newRoom = [[0 for _ in range(CC)] for _ in range(RR)]
    for r in range(RR):
        for c in range(CC):
            if room[r][c]>4: # 5 이상의 미세먼지면 확산
                dust = room[r][c]
                move = dust//5
                cnt = 0
                for dc, dr in dir:
                    nc, nr = c+dc, r+dr
                    if nc<0 or nc>=CC or nr<0 or nr>=RR:
                        continue
                    if room[nr][nc]==-1:
                        continue
                    newRoom[nr][nc]+=move
                    cnt+=1
                room[r][c]=dust-move*cnt
    for r in range(RR):
        for c in range(CC):
            room[r][c]+=newRoom[r][c]


def main(room):
    for t in range(TT):
        dustMove(room)
        operateCleaner()
    ans = 0
    for i in room:
        ans += sum(i)
    return(ans+2)


if '__main__'==__name__:
    RR, CC, TT = map(int, input().split())
    room = []
    cleaner = []
    dir = [(0,-1),(0,1),(-1,0),(1,0)] # 상하좌우 c,r
    for i in range(RR):
        temp = list(map(int, input().split()))
        if temp[0]==-1:
            cleaner.append(i)  # r
        room.append(temp)
    print(main(room))