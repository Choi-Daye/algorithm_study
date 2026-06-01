def solution(phone_book):
    hash = {}
    for num in phone_book:
        hash[num] = True
    
    for num in phone_book:
        search = ""
        for n in num[:-1]:  # 자기자신 제외
            search += n
            if search in hash:
                return False
    return True