def solution(participant, completion):
    player = {}
    
    for name in participant:
        player[name] = player.get(name, 0) + 1

    for name in completion:
        player[name] -= 1
    
    for name in player:
        if player[name] == 1:
            return name