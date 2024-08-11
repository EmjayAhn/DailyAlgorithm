import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
books = deque(map(int, sys.stdin.readline().split()))
books = sorted(books)

length = 0

while books:
    for _ in range(M):
        position = books.popleft()
        
        
        
    
    
print(books)
