# corrected_one_step.py
import sys

def total(A, B):
    """Return sum_i A[i]*B[i] as integer."""
    s = 0
    for a, b in zip(A, B):
        s += a * b
    return s

def one_step_best(A, B):
    """
    Consider all valid single-unit operations:
      - reduce A[i] by 1 if A[i] > 0
      - reduce B[i] by 1 if B[i] > 0
    Return a tuple (best_total, best_i, best_type, newA, newB)
    where best_type is 'A' or 'B'. If no operation possible (all zero), return None.
    """
    n = len(A)
    cur_total = total(A, B)
    best_total = cur_total
    best_i = -1
    best_type = None
    bestA = None
    bestB = None

    # Try every possible single decrement
    for i in range(n):
        a = A[i]
        b = B[i]
        if a > 0:
            # simulate reducing A[i]
            newA = A.copy()
            newA[i] = a - 1
            t = total(newA, B)
            if t < best_total:
                best_total = t
                best_i = i
                best_type = 'A'
                bestA = newA
                bestB = B.copy()
        if b > 0:
            # simulate reducing B[i]
            newB = B.copy()
            newB[i] = b - 1
            t = total(A, newB)
            if t < best_total:
                best_total = t
                best_i = i
                best_type = 'B'
                bestA = A.copy()
                bestB = newB

    if best_type is None:
        return None  # no valid operation
    return best_total, best_i, best_type, bestA, bestB

def simulate_k_steps(A_orig, B_orig, k):
    """
    Apply one-step-best greedily for k steps (or until no operations possible).
    Returns (final_total, finalA, finalB).
    """
    A = A_orig.copy()
    B = B_orig.copy()

    for step in range(k):
        res = one_step_best(A, B)
        if res is None:
            break
        best_total, best_i, best_type, newA, newB = res
        A, B = newA, newB
    return total(A, B), A, B

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    N = int(next(it))
    Q = int(next(it))
    A = [int(next(it)) for _ in range(N)]
    B = [int(next(it)) for _ in range(N)]
    queries = [int(next(it)) for _ in range(Q)]

    # For each query, start from fresh original arrays (typical contest expectation)
    for X in queries:
        final_total, finalA, finalB = simulate_k_steps(A, B, X)
        print(final_total if final_total >= 0 else 0)

if __name__ == "__main__":
    main()
