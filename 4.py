from itertools import permutations


def gen_bananas(find_in, find_str):
    hyphens = len(find_in) - len(find_str)
    for perm in permutations(range(len(find_in)), hyphens):
        temp_list = [i for i in find_in]
        for pe in perm:
            temp_list[pe] = '-'
        yield temp_list


def bananas(s) -> set:
    result = set()
    # Your code here!
    for candidat in gen_bananas(s, 'banana'):
        if (candidat.count('b'), candidat.count('a'), candidat.count('n')) == (1, 3, 2):
            if [char for char in candidat if char != '-'] == [letter for letter in 'banana']:
                result.add(''.join(candidat))
    return result


if __name__ == '__main__':
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                    "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                    "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
