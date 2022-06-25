import random
from itertools import permutations


def d6():
    return random.randint(1, 6)


def roll():
    """Roll 4d6kh3"""
    return sum(sorted((d6() for _ in range(4)))[1:])


def generate_array():
    array = sorted((roll() for _ in range(6)))
    total = sum(array)
    lower, upper = 62, 82
    while not (lower < total < upper):
        print(f"Generated: {array}, total: {total}")
        if lower >= total:
            print(f"Too low, replacing lowest: {array[0]}")
            array[0] = roll()
        else:
            print(f"Too high, replacing second highest: {array[-2]}")
            array[-2] = roll()

        array = sorted(array)
        total = sum(array)

    print(f"Final array: {array}, total: {total}")
    return array


if __name__ == "__main__":
    array = generate_array()
    permutations_ = tuple(permutations(array, 6))
    for _ in range(5):
        print(random.choice(permutations_))
