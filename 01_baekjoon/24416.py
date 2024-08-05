import sys

def fibonacci_recursive(n):
    global recursive_count
    
    if n == 1 or n == 2:
        recursive_count += 1
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    
def fibonacci_dynamic(n):
    global dynamic_count
    dp = [0] * (n+1)
    dp[1] = 1; dp[2] = 1;
    for i in range(3, n+1):
        dynamic_count += 1
        dp[i] = dp[i-1]  +  dp[i-2]
        
    return dp[n]
    
        

input = sys.stdin.readline
N = int(input())
recursive_count = 0
dynamic_count = 0
fibonacci_recursive(N)
fibonacci_dynamic(N)
print(recursive_count, end=' ')
print(dynamic_count)