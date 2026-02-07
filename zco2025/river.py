# Example input:
'''
N=5 M=3 K=10 B=1
1 2 TIME = 2
7 4 TIME = 4
4 3 TIME = 2
9 9 TIME = 1
0 0 TIME = 1

H H X X H X X H X H
- - - | - - - - - -
W X W W W X X X X W

solution:
1. For all possible Hi Wi we will get time taken using normal way.
2. then for all L that can exist (L can only feasibly exist at existing Hi or Wi values) we will get the time taken for every Hi Wi combo using new route.
3. We will sort these values.
4. For all of these L, we will check the Mth person in the sorted list of new times and get a differnece from that new time and old time. after storing these differences, we get least difference and that is T.

'''
# input management
first_line = list(map(int, input().split()))
N = first_line[0]
M = first_line[1]
K = first_line[2]
B = first_line[3]
values = []
for i in range(N):
    values.append(list(map(int, input().split())))

# Part 1, get time taken per entry 
'''
formula to get time taken for H and W

abs(H - W) + 1
'''
time_taken = []
distinct_H_W = set()
for value in values:
    H = value[0]
    W = value[-1]
    distinct_H_W.add(H)
    distinct_H_W.add(W)
    time = abs(H-W) + B
    time_taken.append(time)

timeee = time_taken # by boat

# Part 2
all_coords = list(distinct_H_W)
min_coord = min(all_coords)
max_coord = max(all_coords)
possible_L = range(min_coord, max_coord + 1)

'''
formula to get the time taken for H to W USING L as bridge

first caluclate time from H to L:
abs(H - L)

then calculate time from L to W:
abs(L - W)

then we add B for time taken to cross Bridge
+ 1

so:
abs(H-L) + abs(L-W) + B is new time.
'''
tollerance_perL = []
for L in possible_L:
    time_value = []
    for index, value in enumerate(values):
        H = value[0]
        W = value[-1]
        time = abs(H-L) + abs(L-W) + 1
        time_value.append(time-timeee[index])
    time_value.sort()
    tollerance_perL.append(time_value)
    

T = 0
T = min(tol[M-1] for tol in tollerance_perL)
print(max(0,T))