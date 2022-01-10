import random

if __name__ == '__main__':
    n = int(input("이번 주 문제 개수를 입력해주세요: "))
    names = ["김예희",
             "이서영",
             "임현강",
             "정우용",
             "홍지연"]
    weights = {}
    for name in names:
        weights[name] = 2.0
    is_presented_people_last_time = True \
        if input("지난 주에 발표한 사람이 있습니까? (Y/N): ") == "Y" \
        else False
    if is_presented_people_last_time:
        presented_people = list(input("발표한 사람의 이름을 입력하세요: ")
                                for _ in range(n))
        for presented_person in presented_people:
            weights[presented_person] = 1.0
    presenters = []
    for _ in range(n):
        presenter = random.choices(names, weights=list(weights.values()))[0]
        presenters.append(presenter)
        del weights[presenter]
        names.remove(presenter)
    print("\n이번 주에 발표할 사람은...")
    random.shuffle(presenters)
    for i, presenter in enumerate(presenters):
        print(f"<{presenter}>님, {i + 1}번째 문제 발표입니다. 축하드립니다!!")
