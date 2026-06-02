def solution(numbers, target):
    
    def calculate(index, current_sum):
        if index == len(numbers):
            if current_sum == target:
                return 1
            else:
                return 0
        
        plus_way = calculate(index+1, current_sum + numbers[index])
        minus_way = calculate(index+1, current_sum - numbers[index])
        
        return plus_way + minus_way
    
    return calculate(0, 0)