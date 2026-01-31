import sys
#input management
nq, A_i, B_i = list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))
N, Q = nq[0], nq[1]
X_j = []
for i in range(Q):
    X_j.append(int(input()))
#-----------------------------
'''
LOGIC
func total()



'''

def total(A_list, B_list):
    n = len(A_list)
    output = 0
    for i in range(n):
        output+=A_list[i]*B_list[i]
    return output

def best_step(A_list, B_list):
    n=len(A_list)
    currn_total = total(A_list, B_list)
    best_total = currn_total
    best_i = -1
    bestA = None
    bestB = None
    best_type = None

    for i in range(n):
        a = A_list[i]
        b = B_list[i]
        if a>0:
            # option 1
            newA = A_list.copy()
            newA[i] = a-1
            new_total = total(newA, B_list)
            if new_total< best_total:
                best_total = new_total
                best_i = i
                bestA = newA
                bestB = B_list.copy()
                best_type = 'A'
        if b>0:
            #option 2
            newB = B_list.copy()
            newB[i] = b-1
            new_total = total(A_list, newB)
            if new_total<best_total:
                best_total = new_total
                best_i = i
                bestA = A_list.copy()
                bestB = newB
                best_type = 'B'
        
    if best_type is None:
        return None
    return best_total, bestA, bestB

def go_through_steps(A_list,B_list, steps):
    A = A_list.copy()
    B = B_list.copy()
    for step in range(steps):
        inp = best_step(A,B)
        if inp is None:
            break
        best_total = inp[0]
        bestA = inp[1]
        bestB = inp[2]
        A, B = bestA, bestB
    return total(A, B), A, B

for X in X_j:
    final_total = go_through_steps(A_i, B_i, X)

    print(final_total[0]) if final_total[0]>=0 else print(0)