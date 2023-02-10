import random
N = random.randint(0,10)
for x in range(0,N,1):
    N = random.randint(0,10)
    A = []
    A.append(x)
for i in range(N-1):
    m = 11
    if i < m:
        m = A[i]
        A[m] = A[i]
        A[i] = m
