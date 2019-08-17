# https://www.acmicpc.net/problem/3009

dots = []
for _ in range(3):
    dots.append(tuple(map(int, input().split())))

def find_square(dots):
    x_counts = {}
    y_counts = {}
    return_x = 0
    return_y = 0

    for dot in dots:
        try:
            x_counts[dot[0]] += 1
        except:
            x_counts[dot[0]] = 1

        try:
            y_counts[dot[1]] += 1
        except:
            y_counts[dot[1]] = 1
    
    for index, value in x_counts.items():
        if value != 2:
            return_x = index
    for index, value in y_counts.items():
        if value != 2:
            return_y = index
    return return_x, return_y

x, y = find_square(dots)
print(x, y)
            