import sys
#input management
nq, A_i, B_i = list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))
N, Q = nq[0], nq[1]
X_j = []
for i in range(Q):
    X_j.append(int(input()))
#-----------------------------
'''
Logic
TEST CASE
N=4 Q=2
A_i = 2 4 5 3
B_i = 5 2 3 3
X_1 = 1
X_2 = 2

Total B Sum: 42

CORRECT SOLUTION (FOR NOW)
1. get sum of all A_i B_i pairs (here: [7, 6, 8, 6])
2. iterate through N and check if sum of A_n and B_n = highest sum.
3. if so, lucky_veggie = A_n, lucky_water = B_n (here: A_n = 5, B_n = 3)

OPT 1
1. subtract one from lucky_veggie (5)
2. recalculate full B sum which is: 39

OPT 2
1. subtract one from lucky_water (3)
2. recalculate full B sum which is: 37

Get min of results of both options and return that, here 37


'''

def calculate(length, A_list, B_list): # calculates total B for any A and B list
    sume = 0
    for i in range(length):
        sume+=A_list[i]*B_list[i]
    return sume

def upgrade(length, A_list, B_list):
    sum_pairs = []
    for i in range(length):
        sum_pairs.append(A_list[i]*B_list[i])
    max_sum = max(sum_pairs)
    for i in range(length):
        if not A_list[i]*B_list[i] == max_sum:
            continue
        lucky_veggie = A_list[i]
        lucky_water = B_list[i]


        # OPTION 1
        temp_A_list = A_list.copy()
        temp_A_list[i] = A_list[i]-1
   
        opt1_sum = calculate(length, temp_A_list, B_list)

        # OPTION 2
        temp_B_list = B_list.copy()
        temp_B_list[i] = B_list[i]-1
        opt2_sum = calculate(length, A_list, temp_B_list)

        min_list = min(opt1_sum, opt2_sum)
        if min_list == opt1_sum:
            return min_list, temp_A_list, B_list
        else:
            return min_list, A_list, temp_B_list
A_i_temp = A_i.copy()
B_i_temp = B_i.copy()
for j in range(5):
    answer = upgrade(N, A_i_temp, B_i_temp)
    A_i_temp = answer[1]
    B_i_temp = answer[2]
print(answer[0]) if answer[0]>=0 else print(0)
sys.exit()
for X in X_j: 
    A_i_temp = A_i.copy()
    B_i_temp = B_i.copy()
    for j in range(X):
        answer = upgrade(N, A_i_temp, B_i_temp)
        A_i_temp = answer[1]
        B_i_temp = answer[2]
    print(answer[0]) if answer[0]>=0 else print(0)