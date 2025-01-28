# Dice Probability

You throw a dice n times, and every throw produces an outcome between 1 and 6. What is the probability that the sum of outcomes is between a and b?

This problem requires mathematical calculations to determine the probabilities of specific sums. After some research, I discovered the following formula:

$$
P(S, n) = \frac{1}{6^n} \sum_{k=0}^{\lfloor \frac{S-n}{6} \rfloor} (-1)^k \binom{n}{k} \binom{S - 6k - 1}{n-1}
$$

However, the question states that we want the probability of the sum in the range of [a, b]. To do this I just found the sum for each number in the range:

$$
P(\text{range}) = \sum_{S=a}^b P(S, n)
$$

The last formula was the combinations:

$$
\binom{n}{r} = \frac{n!}{r!(n-r)!}
$$

# Code implementation

The first thing I had to do was calculate each number's factorials for the combinations.

My original design had a function that returned the factorial of a number however when dealing with larger values, I found out that it wasn't very efficient recalculating factorials and sometimes led to floating-point errors.

Anyway here is the way I approached calculating factorials:

```py
mF = 6*n # Maximum factorial needed
facs = [1]*(mF+1)
for i in range(2, mF+1):
    facs[i] = facs[i-1] * i
```

Then I created a function for combinations using the formula mentioned earlier:

```py
def chooses(x, y):
    return facs[x] // (facs[y]*facs[x-y])
```

Now this is the main part of the problem where I calculate the probability of a sum:

```py
def PS(S, n):
    sig = 0
    l = (S - n) // 6
    for k in range(l + 1):
        term = chooses(n, k) * chooses(S-6 * k-1, n-1)
        sig += term * (-1) ** k
    return sig / (6 ** n)
```

And finally we repeat this for each number in the range, adding the probabilities to a total:

```py
ans = 0
for num in range(a, b+1):
    ans += PS(num, n)
```
