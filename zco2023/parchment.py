#input management
N, A = list(map(int, input().split()))

integers = list(map(int, input().split()))
Q = int(input())

all_F = []
for _ in range(Q):
    all_F.append(int(input()))

'''
INPUT: 
N: number of ints on parchment
A: max possible int on parchment

integers: the ints
all_F: no of times u can use device

OUTPUT:
min K for all F

'''

'''
DRY RUN
N=6 A=10
ints = 7 4 1 8 5 2
Q=4
all_F:
1
2
5
9

ALGO:
for all possible values of K:
    maintain seperate copied local list of ints
    our_F = 0
    while our_F<F:
        X = min(ints)
        rangee = range(X, X+K+1)
        for index, i in enumerate(ints):
            if i in rangee:
                remove int[index]
        F+=1
    if our_F == F:
        if ints == []:
            return K
'''
def our_algo(F, integers):
    for K in range(0, A):
        ints = integers.copy()
        ints.sort()
        our_F = 0
        while our_F < F:
            if ints == []:
                break
            X = ints[0] # min of ints
            rangee = range(X, X+K+1) 

            ints = [n for n in ints if n not in rangee]
            our_F+=1
        if ints == []:
            return K
for F in all_F:
    print(our_algo(F, integers))

'''
DRY RUN
ints = 7 4 1 8 5 2
F = 1

for all values of k so k = 0
our f = 0
x = 1
rangee = [1, 1]
new ints = 7 4 8 5 2
our_f = 1
ints is not empty so we move to next value of K

k = 1
our f = 0
x = 1
rangee = [1, 2]
new_ints = 7 4 8 5
our_f = 1
ints is not empty so we move to next value of K

...

k = 7
our f = 0
x = 1
rangee = [1, 8]
new_ints = []
our_f = 1
ints is empty, so return K

'''

'''
FAILED
take max of int
sub 1 from it (let y = this)
for every F we take floor(y/f) as K


max_int = max(integers)
this = max_int-1
import math
for F in all_F:
    calc = this/F
    print(math.floor(calc))
'''

