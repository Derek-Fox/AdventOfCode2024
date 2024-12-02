from collections import Counter


def calc_similarity(list1: list[int], list2: list[int]) -> int:
    list2_counts = Counter(list2)
    similarity = 0
    for number in list1:
        similarity += number * list2_counts[number]
    return similarity


def calc_dist(list1: list[int], list2: list[int]) -> int:
    dist = 0
    for num1, num2 in zip(list1, list2):
        dist += abs(num1 - num2)
    return dist


def split_lists(lines: list[str]) -> tuple[list[int], list[int]]:
    list1, list2 = zip(*(map(int, line.split('   ')) for line in lines))
    return list(list1), list(list2)


def get_input(filepath: str) -> list[str]:
    with open(filepath, 'r') as file:
        lines = file.read().splitlines()
    return lines


def part1(list1, list2):
    list1.sort()
    list2.sort()

    dist = calc_dist(list1, list2)
    print(f'Part 1 answer: {dist}')


def part2(list1, list2):
    similarity = calc_similarity(list1, list2)
    print(f'Part 2 answer: {similarity}')


def main():
    filepath = './day1.in'
    lines = get_input(filepath)

    list1, list2 = split_lists(lines)

    # part1(list1, list2)

    part2(list1, list2)


if __name__ == '__main__':
    main()
