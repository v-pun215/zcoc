# input management
N, P = list(map(int, input().split()))
A, B = [], []
for _ in range(N):
    inp = list(map(int, input().split()))
    A.append(inp[0])
    B.append(inp[1])

def calculate_composite_scores(r, A, B, N):
    output = []
    for i in range(N):
        A_score = A[i]
        B_score = B[i]
        out = ((A_score*r) + B_score*(100-r))/100
        output.append(out)
    winner = max(output)
    outee = []
    for index, i in enumerate(output):
        if i == winner:
            outee.append(index+1) # participant number
    return outee
#print(calculate_composite_scores(0, A, B, N))

all_possible_r = range(0,101)
winner_set = set()
for r in all_possible_r:
    winners_r = calculate_composite_scores(r, A, B, N)
    winner_set.update(winners_r)
ma_boi = list(winner_set)
print(len(ma_boi))
print(*ma_boi)