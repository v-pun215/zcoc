import itertools, collections
def generate_all_x(A, B):
    # generate x
    one_list = [1] * len(B)
    zero_list = [0] * len(A)
    naive_x = one_list+zero_list
    return list(set(itertools.permutations(naive_x)))


#print(generate_all_x([1,3], [3,4]))
def interleave(X, A, B):
    n = len(A)
    m = len(B)
    i = 0
    C = [None] * (n + m)
    j = 0
    while (i+j) < (n+m):
        if X[i+j] == 0:
            C[i+j] = A[i]
            i+=1
        else:
            C[i+j] = B[j]
            j+=1
    return C

def calculate_blocks(array):
    blocks = [(key, sum(1 for _ in group)) for key, group in itertools.groupby(array)]
    return len(blocks)
MOD = 10**8 + 7
def solve(n,m,K_target,A,B):

    # dp[i][j][k][last_side]
    # last_side: 0 for A, 1 for B
    dp = [[[[0] * 2 for _ in range(K_target + 2)] for _ in range(m + 1)] for _ in range(n + 1)]

    # Base cases: The first element always starts 1 block
    if n > 0:
        dp[1][0][1][0] = 1
    if m > 0:
        dp[0][1][1][1] = 1

    for i in range(n + 1):
        for j in range(m + 1):
            for k in range(1, K_target + 1):
                # Try adding A[i] to an existing sequence
                if i < n:
                    # Previous was from A
                    if i > 0:
                        new_k = k + (1 if A[i] != A[i-1] else 0)
                        if new_k <= K_target:
                            dp[i+1][j][new_k][0] = (dp[i+1][j][new_k][0] + dp[i][j][k][0]) % MOD
                    # Previous was from B
                    if j > 0:
                        new_k = k + (1 if A[i] != B[j-1] else 0)
                        if new_k <= K_target:
                            dp[i+1][j][new_k][0] = (dp[i+1][j][new_k][0] + dp[i][j][k][1]) % MOD

                # Try adding B[j] to an existing sequence
                if j < m:
                    # Previous was from A
                    if i > 0:
                        new_k = k + (1 if B[j] != A[i-1] else 0)
                        if new_k <= K_target:
                            dp[i][j+1][new_k][1] = (dp[i][j+1][new_k][1] + dp[i][j][k][0]) % MOD
                    # Previous was from B
                    if j > 0:
                        new_k = k + (1 if B[j] != B[j-1] else 0)
                        if new_k <= K_target:
                            dp[i][j+1][new_k][1] = (dp[i][j+1][new_k][1] + dp[i][j][k][1]) % MOD

    ans = (dp[n][m][K_target][0] + dp[n][m][K_target][1]) % MOD
    return ans

# input management
T = int(input())
answers = []
inp = []
for _ in range(T):
    n,m,K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    inp.append([[n,m,K],A,B])
for i in inp:
    n,m,K = i[0]
    A = i[1]
    B = i[2]
    answer = solve(n,m,K,A,B)
    print(answer)