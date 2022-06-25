from functools import reduce
from operator import mul


def primes(numb: int) -> set:
    _set = set()
    for i in range(numb - 1, 1, -1):
        is_simple = 0
        if numb % i == 0:
            for j in range(i - 1, 1, -1):
                if i % j == 0:
                    is_simple = is_simple + 1
            if is_simple == 0:
                _set.add(i)
    return _set


def count_find_num(primesl, lim):
    minimum: int = reduce(mul, primesl)
    _set = set()
    for i in range(minimum, lim + 1):
        if sum(1 for prime in primesl if not i % prime) == len(primesl):
            if primes(i) == set(primesl):
                _set.add(i)
    return [len(_set), max(_set)] if _set else []


if __name__ == '__main__':
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
