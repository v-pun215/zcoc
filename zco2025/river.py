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

print(first_line)
print(values)
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
    time = abs(H-W) + 1
    time_taken.append(time)

print(time_taken)
print(list(distinct_H_W))

# Part 2
possible_L = list(distinct_H_W)

'''
formula to get the time taken for H to W USING L as bridge

first caluclate time from H to L:
abs(H - L)

then calculate time from L to W:
abs(L - W)

then we add B for time taken to cross Bridge
+ B

so:
abs(H-L) + abs(L-W) + B is new time.
'''
time_taken_with_L = []
for L in possible_L:
    time_taken = {}
    for index, value in enumerate(values):
        H = value[0]
        W = value[-1]
        time = abs(H-L) + abs(L-W) + B
        time_taken[index+1] = time
    sorted_items = sorted(time_taken.items(), key=lambda item: item[1])
    sorted_dict = dict(sorted_items)
    time_taken_with_L.append(sorted_dict)

print(time_taken_with_L)
all_threes = []
for value in time_taken_with_L:
    all