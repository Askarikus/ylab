from functools import reduce
from math import sqrt
from operator import mul


def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i <= sqrt(num):
        if num%i == 0:
            return False
        i += 1
    return True

def primes(numb, primesl):
    i = 2
    while i <= (1 + (numb/2)):
        if numb % i == 0:
            if is_prime(i):
                if i not in primesl:
                    return False
        i += 1
    return True


def count_find_num(primesl, lim):
    minimum = reduce(mul, primesl)
    _set = set()
    for i in range(minimum, lim + 1, minimum):
        if sum(1 for prime in primesl if not i % prime) == len(primesl):
            if primes(i, primesl):
                _set.add(i)
    return [len(_set), max(_set)] if _set else []


if __name__ == '__main__':
    # primesL = [2, 3]
    # limit = 200
    # print(count_find_num(primesL, limit))

    primesL = [41, 59, 89]
    limit = 14731875
    print(count_find_num(primesL, limit))
    # result is [3, 12702169]

    primesL = [2, 3]
    limit = 200
    assert count_find_num(primesL, limit) == [13, 192]

    primesL = [2, 5]
    limit = 200
    assert count_find_num(primesL, limit) == [8, 200]

    primesL = [2, 3, 5]
    limit = 500
    assert count_find_num(primesL, limit) == [12, 480]

    primesL = [2, 3, 5]
    limit = 1000
    assert count_find_num(primesL, limit) == [19, 960]

    primesL = [2, 3, 47]
    limit = 200
    assert count_find_num(primesL, limit) == []
