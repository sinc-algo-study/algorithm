import collections
import math


def hhmm_to_minute(hhmm):
    h, m = hhmm.split(":")
    return int(h) * 60 + int(m)


def calculate_fee(time, fees):
    basic_time, basic_fee, unit_time, unit_fee = fees
    if time <= basic_time:
        return basic_fee
    time -= basic_time
    return basic_fee + math.ceil(time / unit_time) * unit_fee


def solution(fees, records):
    record_dict = collections.defaultdict(collections.deque)
    for record in records:
        hhmm, car_number, in_or_out = record.split()
        m = hhmm_to_minute(hhmm)
        record_dict[car_number].append(m)

    LAST_TIME = hhmm_to_minute("23:59")
    answer = []
    for car_number in sorted(record_dict.keys()):
        record = record_dict[car_number]
        time = 0
        while len(record) > 1:
            in_time = record.popleft()
            out_time = record.popleft()
            time += out_time - in_time
        if record:
            time += LAST_TIME - record.popleft()

        answer.append(calculate_fee(time, fees))

    return answer


if __name__ == '__main__':
    fees_list = [
        [180, 5000, 10, 600],
        [120, 0, 60, 591],
        [1, 461, 1, 10]
    ]
    records_list = [
        ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
         "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN",
         "23:00 5961 OUT"],
        ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT",
         "23:58 3961 IN"],
        ["00:00 1234 IN"]
    ]

    for fees, records in zip(fees_list, records_list):
        print(solution(fees, records))
