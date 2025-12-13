def solution(people, limit):
    people.sort()
    start, end = 0, len(people) - 1
    boats = 0

    while start <= end:
        boats += 1  # 보트 하나 사용

        # 가장 가벼운 + 가장 무거운 같이 태울 수 있으면 같이 태움
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            # 아니면 무거운 사람만 태움
            end -= 1

    return boats
