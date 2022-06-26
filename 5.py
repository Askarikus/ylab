from itertools import combinations_with_replacement
from functools import reduce
from operator import mul


def count_find_num(input_list_of_primes, up_limit):
    divisors_set_result = set()
    min_prime = min(input_list_of_primes)
    len_permutations = sum(1 for i in range(1, 100) if min_prime ** i <= up_limit) + 1
    minimum_divisor = reduce(mul, input_list_of_primes)
    input_list_of_primes.append(1)
    all_comb = combinations_with_replacement(input_list_of_primes, len_permutations)
    input_list_of_primes.remove(1)
    for i in all_comb:
        if minimum_divisor <= reduce(mul, i) <= up_limit:
            if (set(i).symmetric_difference(set(input_list_of_primes)) == {1} or
                    set(i).symmetric_difference(set(input_list_of_primes)) == set()):
                divisors_set_result.add(reduce(mul, i))
    return [len(divisors_set_result), max(divisors_set_result)] if divisors_set_result else []


if __name__ == '__main__':
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
