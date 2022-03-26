'''
fees = []*4
records = ["HH:MM 차량번호 IN/OUT", ... ]
출차 없으면 23:59분에 출차한 걸로 침(홀수면, 23*60+59-마지막 꺼)
차량번호 작은 자동차부터 return
! dict 정렬: dict = dict(sorted(dict.items())) => 정렬결과는 리스트므로, dict()씌워서 다시 dict로 만들어야 함
! dict for문 : for key in dict: (키를 가져옴)
! 올림은 import math해서 math.ceil(~)임
! a, b, c = str.split() 가능!!
? len()이랑 인덱싱 중 뭐가 시간복잡도 낮은지? len의 시간복잡도..?!
! defaultDict 제대로 정리해두기!
1. record에서 하나씩 새 딕셔너리에 차량번호 : 시간(시간*60+분)) 입력
2. 딕셔너리 키 오름차순 정렬
3. 맨 첫 번째부터 원소 홀 수 개면, 23*60+59 추가해주고 2*i - 2*i-1 순으로 계산해서 answer에 담기
'''
from collections import defaultdict
def solution(fees, records):
    answer = []
    cars = defaultdict(list)
    last = 23*60+59
    for car in records:
        temp = car.split()
        t, num = temp[0], temp[1]
        timeTmp = t.split(":")
        time = int(timeTmp[0])*60+int(timeTmp[1])
        cars[num].append(time)
    print(cars)
    for key in cars:
        if len(cars[key])%2==1:
            cars[key].append(last)
        car = cars[key]
        total = 0
        for c in range(len(car)-1, -1, -2):
            total += (car[c]-car[c-1])
        answer.append(total)
    return answer

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))