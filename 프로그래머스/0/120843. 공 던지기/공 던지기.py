def solution(numbers, k):
    idx = 2 * (k-1)
    
    while idx >= len(numbers):
        idx %= len(numbers)
    
    return numbers[idx]