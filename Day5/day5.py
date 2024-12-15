def verify_update(rules: dict[int, list[int]], update: list[int]) -> bool:
    print(f'----------{update=}----------')
    for idx, num in enumerate(update[:-1]):
        if num not in rules: continue
        reqs = rules[num]
        after = update[idx + 1:]
        for req in after:
            if req in reqs:
                print(f'Failed on {num=} with {req=} and {after=}')
                print()
                return False
        print(f'{num=}')
        print(f'{reqs=}')
        print(f'{after=}')
        print()
    return True


def part1(rules: dict[int, list[int]], updates: list[list[int]]) -> None:
    total = 0
    for update in updates:
        if not verify_update(rules, update): continue
        total += update[len(update) // 2]
    print(total)


def get_input(filepath: str) -> tuple[dict[int, list[int]], list[list[int]]]:
    rules: dict[int, list[int]] = {}
    with open(filepath, 'r') as file:
        top, bottom = file.read().split('\n\n')

        for rule in top.splitlines():
            req, num = map(int, rule.split('|'))
            rules.setdefault(num, []).append(req)

        updates = [[int(update) for update in line.split(',')] for line in bottom.splitlines()]

    return rules, updates


def main():
    filepath = "day5.in"
    rules, updates = get_input(filepath)

    part1(rules, updates)


if __name__ == '__main__':
    main()
