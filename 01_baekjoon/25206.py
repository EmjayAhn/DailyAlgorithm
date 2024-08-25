import sys
input = sys.stdin.readline

score_map = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0   
}

total_class_score = 0
total_score = 0
for _ in range(20):
    subject, class_score, score = input().split()
    if score != 'P':
        total_class_score += float(class_score)
        total_score += (float(class_score) * score_map[score])
        
print(total_score / total_class_score)