def solution(s):
    answer = len(s)

    # step은 문자열 자를 단위
    # s 길이의 절반보다 큰 단위부터는 볼 필요 없음
    for step in range(1, len(s) // 2 + 1):
        compressed = ""  # 이번 step으로 압축했을 때 결과
        prev = s[:step]  # 우선 step개만큼 자름
        count = 1  # prev가 반복되는 개수
        for i in range(step, len(s), step):
            # 이제 step번째 인덱스(단위만큼 자른 문자열의 다음 글자)부터 step개씩 자르면서
            # 문자열 압축
            now = s[i: i + step]  # step개만큼 자름
            if now == prev:
                # 자른 게 prev와 같다면, count 1 증가
                count += 1
                continue
            # 자른 게 prev와 다르다면, compressed에 {count}{prev}를 붙임
            # 이 때, count가 1이라면 count는 생략
            # 이후 prev에 now를 저장하고 count를 1로 초기화(다시 시작)
            compressed += f"{count}{prev}" if count > 1 else prev
            prev = now
            count = 1
        # 마지막으로 남아 있는 count와 prev를 compressed에 추가
        compressed += f"{count}{prev}" if count > 1 else prev
        # answer 갱신
        answer = min(answer, len(compressed))

    return answer


if __name__ == '__main__':
    ss = [
        "aabbaccc",  # 7
        "ababcdcdababcdcd",  # 9
        "abcabcdede",  # 8
        "abcabcabcabcdededededede",  # 14
        "xababcdcdababcdcd"  # 17
    ]

    for s in ss:
        print("s =", s + ", result =", solution(s))
