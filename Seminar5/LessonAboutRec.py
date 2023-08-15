def summ_rec(N):
    if N == 0:
        return 0
    return N + summ_rec(N-1)

print(summ_rec(4))
