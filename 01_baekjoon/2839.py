def sugar_delivery(N):
    # 5킬로그램 봉지의 최대 개수부터 시작하여 하나씩 줄여가며 확인합니다.
    for i in range(N // 5, -1, -1):
        remaining_sugar = N - (i * 5)
        # 나머지가 3의 배수인지 확인합니다.
        if remaining_sugar % 3 == 0:
            j = remaining_sugar // 3
            return i + j
    return -1

# 예제 실행
N = int(input())
result = sugar_delivery(N)
print(result)