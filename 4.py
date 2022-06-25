from itertools import combinations


def bananas(s) -> set:
    result = set()
    hyphens = len(s) - len('banana')
    for perm in combinations(range(len(s)), hyphens):
        temp_list = list(s)
        for pe in perm:
            temp_list[pe] = '-'
        if 'b' in temp_list:
            if [char for char in temp_list if char != '-'] == list('banana'):
                result.add(''.join(temp_list))
    return result


if __name__ == '__main__':
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                    "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                    "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
