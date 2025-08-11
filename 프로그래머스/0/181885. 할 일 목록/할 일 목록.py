def solution(todo_list, finished):
    return [todo_list[i] for i, check in enumerate(finished) if not(check)]