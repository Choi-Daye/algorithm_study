def solution(nums):
    answer = 0
    
    if len(nums)/2 <= len(set(nums)):
        return len(nums)/2
    else:
        return len(set(nums))