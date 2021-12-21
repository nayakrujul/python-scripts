def get_primes(a, b):

    primes = []

    for num in range(a, b + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)

    return primes


def prime_factors(x):

    factors = []

    if x < 2:
        return -1

    primes = get_primes(1, x)

    for i in primes:
        while x % i == 0:
            factors.append(i)
            x /= i

    return factors


def get_unique(lst):

    unique = []

    for x in lst:
        if x not in unique:
            unique.append(x)

    return unique


def hcf(x, y):

    factors_x = prime_factors(x)
    factors_y = prime_factors(y)

    different_x = dict()
    different_y = dict()

    unique_x = get_unique(factors_x)
    unique_y = get_unique(factors_y)

    for i in unique_x:
        different_x[i] = factors_x.count(i)
    for j in unique_y:
        different_y[j] = factors_y.count(j)

    product = 1

    for a in different_x.keys():
        if a in different_y.keys():
            if different_x[a] <= different_y[a]:
                product *= a ** different_x[a]
            else:
                product *= a ** different_y[a]

    return product


def lcm(x, y):

    return int((x * y) / hcf(x, y))
