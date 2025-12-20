inp = list(map(int, input().split()))
a,b,x,y = inp[0],inp[1],inp[2],inp[3]

dist_tp = abs(x-y)
dist_trac = abs(a-b)

start_trac, end_trac = min(a,b), max(a,b)
start_tp, end_tp = min(x,y), max(x,y)

#is it worth it
if (abs(start_trac-start_tp) + abs(end_trac-end_tp)) < abs(start_trac-end_trac):
    print(abs(start_trac-start_tp) + abs(end_trac-end_tp))
else:
    print(abs(start_trac-end_trac))