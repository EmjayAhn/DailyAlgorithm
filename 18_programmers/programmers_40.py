# https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)    
    truck_weights = deque(truck_weights)
    
    current_weight = 0
    
    while len(truck_weights) > 0:
        time += 1
        current_weight = current 
    
    
    
    
if __name__ == '__main__':
    bridge_length = [2, 100, 100]
    weight = [10, 100, 100]
    truck_weights = [[7, 4, 5, 6], [10], [10,10,10,10,10,10,10,10,10,10]]
    
    for i in range(len(bridge_length)):
        print(solution(bridge_length[i], weight[i], truck_weights[i]))