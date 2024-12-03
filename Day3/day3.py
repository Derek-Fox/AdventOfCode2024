import re


def get_input(filepath: str) -> str:
    with open(filepath, 'r') as file:
        return file.read().replace('\n', '')


def find_muls(memory: str, enable_cond: bool) -> list[str]:
    if enable_cond:
        memory = re.sub("don't\\(\\).*?do\\(\\)", repl='', string=memory)

    pattern = re.compile("mul\\([0-9]+,[0-9]+\\)")
    return pattern.findall(memory)


def eval_muls(muls: list[str]) -> int:
    return sum(a * b for a, b in (map(int, mul[4:-1].split(',')) for mul in muls))

def part1(memory: str):
    valid_muls = find_muls(memory, enable_cond=False)
    print(f'Part 1 answer: {eval_muls(valid_muls)}')


def part2(memory: str):
    valid_muls = find_muls(memory, enable_cond=True)
    print(f'Part 2 answer: {eval_muls(valid_muls)}')


def main():
    filepath = './day3.in'
    memory = get_input(filepath)

    part1(memory)
    part2(memory)


if __name__ == '__main__':
    main()
