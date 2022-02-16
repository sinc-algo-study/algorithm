"""
1. hh:mm:ss -> 초로 변환하여 생각
2. 동영상 재생시간은 최대 99:59:59이므로 최대 100*60*60초 = 360000초까지임
3. ad[360000] 배열을 0으로 초기화
    - ad[i] = n : i초에 시청자 수가 n명
4. logs로부터 ad 배열을 구하고, 누적합을 구함
5. 누적합을 이용하여 ad배열을 adv_time씩 확인해가며 최대 시청자 수(=최대 누적 재생시간)를 구함
"""


def hhmmss_to_second(hhmmss):
    hh, mm, ss = hhmmss.split(":")
    return int(hh) * 3600 + int(mm) * 60 + int(ss)


def second_to_hhmmss(second):
    hhmmss = f"{str(second // 3600).zfill(2)}:"
    second %= 3600
    hhmmss += f"{str(second // 60).zfill(2)}:"
    second %= 60
    hhmmss += str(second).zfill(2)
    return hhmmss


def solution(play_time, adv_time, logs):
    play_time = hhmmss_to_second(play_time)
    adv_time = hhmmss_to_second(adv_time)
    ad = [0] * (SIZE + 1)
    for log in logs:
        start, end = map(hhmmss_to_second, log.split("-"))
        # 시청 시작 초 start에는 시청자수 +1
        ad[start] += 1
        # 시청 종료 초 end에는 시청자수 -1
        ad[end] -= 1
    for i in range(1, SIZE + 1):
        # 위의 start, end 체크를 바탕으로 모든 구간에 시청자수를 기록
        # start ~ end - 1까지는 1이 되고, end초에는 0이 될거임
        ad[i] += ad[i - 1]
    for i in range(1, SIZE + 1):
        # 기록된 시청자 수 ad배열을 기반으로 누적합을 구함
        ad[i] += ad[i - 1]

    max_time = ad[adv_time - 1]
    answer = 0
    for i in range(play_time - adv_time + 1):
        # 누적 합으로 광고 재생 시간 동안의 누적 시청자 수를 구해서 비교
        tmp = ad[i + adv_time] - ad[i]
        if tmp > max_time:
            max_time = tmp
            answer = i + 1

    return second_to_hhmmss(answer)


if __name__ == '__main__':
    SIZE = 100 * 60 * 60
    play_times = ["02:03:55", "99:59:59", "50:00:00"]
    adv_times = ["00:14:15", "25:00:00", "50:00:00"]
    logs_list = [
        ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29",
         "01:30:59-01:53:29", "01:37:44-02:02:30"],
        ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59",
         "11:00:00-31:00:00"],
        ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
    ]
    for play_time, adv_time, logs in zip(play_times, adv_times, logs_list):
        print(solution(play_time, adv_time, logs))
