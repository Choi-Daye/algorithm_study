def solution(phone_book):
    phone_book.sort()
    
    for i, head_num in enumerate(phone_book):
        if i == len(phone_book)-1:
            break
        if head_num == phone_book[i+1][:len(head_num)]:
            return False
    return True