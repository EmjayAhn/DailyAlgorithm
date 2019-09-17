# https://www.acmicpc.net/problem/10866

import sys

class Deque():
    def __init__(self):
        self.items = []

    def push_front(self, input):
        temp = []
        temp.append(input)
        self.items = temp + self.items

    def push_back(self, input):
        self.items.append(input)

    def pop_front(self):
        if self.items:
            result = self.items[0]
            print(result)
            del self.items[0]
        else:
            print(-1)
    
    def pop_back(self):
        if self.items:
            result = self.items[-1]
            print(result)
            del self.items[-1]
        else:
            print(-1)
    
    def size(self):
        print(len(self.items))

    def empty(self):
        if self.items:
            print(0)
        else:
            print(1)

    def front(self):
        if self.items:
            print(self.items[0])
        else:
            print(-1)

    def back(self):
        if self.items:
            print(self.items[-1])
        else:
            print(-1)


N = int(sys.stdin.readline().rstrip())
deque = Deque() 
for _ in range(N):
    commands = sys.stdin.readline().rstrip().split()
    if len(commands) == 1:
        command = 'deque.' + commands[0] + '()'
        command = eval(command)
        command
    else:
        command = 'deque.' + commands[0] + '({})'.format(commands[1])
        command = eval(command)
        command



    
