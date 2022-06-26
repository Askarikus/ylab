from functools import reduce
from math import sqrt
from operator import mul

set_of_primes = {2}


def is_prime(num):
    if num <= 1:
        return False
    i = 2
    sqrt_num = sqrt(num)
    while i <= sqrt_num:
        if num % i == 0:
            return False
        i += 1
    return True


def primes(number, input_list_of_primes):
    _set_of_primes_divisors = set()
    for element in set_of_primes:
        if number % element == 0:
            if element not in input_list_of_primes:
                return False
            else:
                _set_of_primes_divisors.add(element)
    return _set_of_primes_divisors == set(input_list_of_primes)


def count_find_num(input_list_of_primes, up_limit):
    divisors_set_result = set()
    minimum_divisor = reduce(mul, input_list_of_primes)
    if (sqrt(up_limit) + 100) > max(set_of_primes):
        for n in range(int(sqrt(up_limit) + 100), max(set_of_primes), -1):
            if is_prime(n):
                set_of_primes.add(n)
    for i in range(minimum_divisor, up_limit + 1, minimum_divisor):
        if primes(i, input_list_of_primes):
            divisors_set_result.add(i)
    return [len(divisors_set_result), max(divisors_set_result)] if divisors_set_result else []


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
