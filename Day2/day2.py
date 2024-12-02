import sys


def parse_reports(lines: list[str]) -> list[list[int]]:
    return [list(map(int, line.split())) for line in lines]


def get_input(filepath: str) -> list[str]:
    with open(filepath, 'r') as file:
        return file.read().splitlines()


def validate_diff(curr_diff: int, first_diff: int) -> bool:
    if curr_diff == 0: return False
    if not (1 <= abs(curr_diff) <= 3): return False
    if (curr_diff < 0) != (first_diff < 0): return False
    return True


def validate_report(report: list[int], allowed_errors=0) -> bool:
    if len(report) < 2: return True

    initial_diff = report[1] - report[0]

    for i in range(len(report) - 1):
        current_diff = report[i + 1] - report[i]

        if validate_diff(current_diff, initial_diff): continue

        if allowed_errors == 0: return False

        for offset in range(-1, 2):
            modified_report = report[:i + offset] + report[i + offset + 1:]
            if validate_report(modified_report, allowed_errors - 1): return True

        return False

    return True


def part1(reports: list[list[int]]):
    num_safe = sum([1 if validate_report(report) else 0 for report in reports])
    print(f'Part 1 answer: {num_safe}')


def part2(reports: list[list[int]]):
    num_safe = sum([1 if validate_report(report, allowed_errors=1) else 0 for report in reports])
    print(f'Part 2 answer: {num_safe}')


def main():
    filepath = './day2.in'
    lines = get_input(filepath)

    reports = parse_reports(lines)

    part1(reports)
    part2(reports)


if __name__ == '__main__':
    main()
