# https://www.acmicpc.net/problem/4375

def one(num):
    temp = '1'
    answer = 0
    
    while True:
        if int(temp) % num == 0:
            answer = len(temp)
            break
        temp += '1'
        
    return answer

if __name__ == "__main__":
    while True:
        try:
            num = int(input())
            print(one(num))
        except EOFError:
            break