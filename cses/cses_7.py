# Two Knights (how scary!)
def get_all_possible_positions(k):
    return ((k**2) * ((k**2)-1))//2

def solve(k):
    if k==1:
        return 0
    return get_all_possible_positions(k) - 4*(k-1)*(k-2)
n = int(input())
for i in range(1, n+1):
    print(solve(i))
