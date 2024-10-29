import sys
input = sys.stdin.readline

cycle = int(input())

while cycle:
    cycle -= 1
    number = int(input())
    min, mid, max = 0, 0, number
    while True:
        mid = (min + max) // 2
        if (mid*(mid + 1)) //2 < number:
            if ((mid+1)*(mid+2)) // 2 > number:
                break
            else:
                min = mid + 1
        elif (mid*(mid + 1)) //2 > number:
            max = mid - 1
        else:
            break
    print(mid)