def solution(phone_number):
    hide = '*' * (len(phone_number)-4)
    for n in phone_number[len(phone_number)-4:]:
        hide += n
    return hide