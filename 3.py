def zeros(n):
    return sum(n//i for i in (5**x for x in range(1, 15) if 5**x < n))


if __name__ == '__main__':
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
