from collections import defaultdict
from math import ceil


def solution(fees, records):
    def convert_time(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m

    car = defaultdict(list)
    ans = defaultdict(int)
    for record in records:
        time, num, flag = record.split()
        if flag == "IN":
            car[num].append(convert_time(time))
        else:
            ans[num] += (convert_time(time) - car[num].pop())

    for k, v in car.items():
        if v:
            ans[k] += (convert_time("23:59") - v[0])
        # 주차 요금 계산
        price = fees[1]
        if ans[k] > fees[0]:
            price += ceil((ans[k] - fees[0]) / fees[2]) * fees[3]
        ans[k] = price

    res = sorted(ans.items())
    return [x[1] for x in res]






print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))