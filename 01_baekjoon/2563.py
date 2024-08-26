N = int(input())
array = [[0] * 100 for _ in range(100)]  # 도화지 범위 초기화
for _ in range(N):  # 입력 받은 도화지 개수만큼 돈다.
    y1, x1 = map(int, input().split())  # 왼쪽아래 x,y 좌표를 받는다.

    for i in range(x1, x1 + 10):  # 세로를 돈다.
        for j in range(y1, y1 + 10):  # 가로를 돈다.
            array[i][j] = 1  # 해당 범위 값을 0에서 1로 바꿔준다.

result = 0  # 넓이를 출력할 변수
for k in range(100):  # 전체 도화지를 돌면서
    result += array[k].count(1)  # 1 개수만 세어준다

print(result)