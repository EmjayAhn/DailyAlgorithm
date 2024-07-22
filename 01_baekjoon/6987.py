from itertools import combinations

def DFS(home,away):
    global L, tmp
    
    if away==6:
        home+=1
        away=home+1
    
    if home==5:
        if L==[ [0,0,0] for _ in range(6) ]:
            tmp=1
        return

    #home이 이긴경우
    if L[home][0]>0 and L[away][2]>0:
        L[home][0], L[away][2] = L[home][0]-1, L[away][2]-1
        DFS(home,away+1)
        L[home][0], L[away][2] = L[home][0]+1, L[away][2]+1
    
    #home이 지는경우
    if L[home][2]>0 and L[away][0]>0:
        L[home][2], L[away][0] = L[home][2]-1, L[away][0]-1
        DFS(home,away+1)
        L[home][2], L[away][0] = L[home][2]+1, L[away][0]+1
    
    #비기는 경우
    if L[home][1] and L[away][1]>0 :
        L[home][1], L[away][1] = L[home][1]-1, L[away][1]-1
        DFS(home,away+1)
        L[home][1], L[away][1] = L[home][1]+1, L[away][1]+1

sol = []
for round in range(4):
    question = list(map(int, input().split())) 
    L = []
    for i in range(6):
        L.append([question[i*3],question[(i*3)+1],question[(i*3)+2] ])
    
    tmp = 0
    DFS(0,1)
    sol.append(tmp)
    
print(*sol)