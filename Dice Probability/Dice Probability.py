n, a, b = map(int, input().split())
#print(n, a, b)

import math

mF = 6*n
facs = [1]*(mF+1)
for i in range(2, mF+1):
    facs[i] = facs[i-1] * i

def chooses(x, y):
    return facs[x] // (facs[y]*facs[x-y])

#print(chooses(5, 2))

def PS(S, n):
    sig = 0
    l = (S - n) // 6
    for k in range(l + 1):
        term = chooses(n, k) * chooses(S-6 * k-1, n-1)
        sig += term * (-1) ** k
    #print(sig)
    return sig / (6 ** n)

ans = 0
for num in range(a, b+1):
    ans += PS(num, n)

print(f"{ans:.6f}")