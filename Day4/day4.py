class WordSearch:
    def __init__(self, word_search: list[list[str]]):
        self.word_search = word_search

    def in_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < len(self.word_search) and 0 <= col < len(self.word_search[0])

    def keep_expanding(self, pos: tuple[int, int], dir: tuple[int, int], have_letter: str) -> int:
        new_row, new_col = pos[0] + dir[0], pos[1] + dir[1]
        if not self.in_bounds(new_row, new_col): return 0

        next_letter = self.word_search[new_row][new_col]
        match have_letter:
            case 'A':
                return 0 if next_letter != 'S' else 1
            case 'M':
                return 0 if next_letter != 'A' \
                    else self.keep_expanding((new_row, new_col), dir, 'A')
            case 'X' | 'S':
                return 0

    def expand_from_X(self, row: int, col: int) -> int:
        directions = [(d_row, d_col) for d_row in range(-1, 2) for d_col in range(-1, 2) if
                      not (d_row == 0 and d_col == 0)]
        total = 0
        for d_row, d_col in directions:
            new_row, new_col = row + d_row, col + d_col
            if not self.in_bounds(new_row, new_col): continue
            if self.word_search[new_row][new_col] == 'M':
                total += self.keep_expanding((new_row, new_col), (d_row, d_col), 'M')
        return total

    def part1(self) -> None:
        total = 0
        for row, line in enumerate(self.word_search):
            for col, c in enumerate(line):
                if c == 'X':
                    total += self.expand_from_X(row, col)
                    self.word_search[row][col] = '.'
        print(total)

    def find_Ss(self, pos: tuple[int, int], dir: int, cas) -> int:
        curr_row = pos[0]
        curr_col = pos[1]
        match cas:
            case 'd':
                new_row = curr_row + dir
                if not (self.in_bounds(new_row, curr_col - 1) and self.in_bounds(new_row, curr_col + 1)): return 0
                return 1 if self.word_search[new_row][curr_col - 1] == 'S' and self.word_search[new_row][
                    curr_col + 1] == 'S' else 0
            case 'r':
                new_col = curr_col + dir
                if not (self.in_bounds(curr_row - 1, new_col) and self.in_bounds(curr_row + 1, new_col)): return 0
                return 1 if self.word_search[curr_row - 1][new_col] == 'S' and self.word_search[curr_row + 1][
                    new_col] == 'S' else 0
        raise Exception('How?')

    def find_A(self, pos: tuple[int, int], dir: tuple[int, int]) -> int:
        curr_row, curr_col = pos[0], pos[1]
        match dir:
            case (0, 2):
                for offset in [-1, 1]:
                    new_row, new_col = curr_row + offset, curr_col + 1
                    if not self.in_bounds(new_row, new_col): continue
                    if self.word_search[new_row][new_col] == 'A':
                        return self.find_Ss((new_row, new_col), offset, 'd')
            case (2, 0):
                for offset in [-1, 1]:
                    new_row, new_col = curr_row + 1, curr_col + offset
                    if not self.in_bounds(new_row, new_col): continue
                    if self.word_search[new_row][new_col] == 'A':
                        return self.find_Ss((new_row, new_col), offset, 'r')
        return 0

    def find_Ms(self, row: int, col: int) -> int:
        directions = [(0, 2), (2, 0)]
        total = 0
        for d_row, d_col in directions:
            new_row, new_col = row + d_row, col + d_col
            if not self.in_bounds(new_row, new_col): continue
            if self.word_search[new_row][new_col] == 'M':
                total += self.find_A((row, col), (d_row, d_col))
        return total

    def part2(self) -> None:
        total = 0
        for row, line in enumerate(self.word_search):
            for col, c in enumerate(line):
                if c == 'M':
                    total += self.find_Ms(row, col)
                    self.word_search[row][col] = '.'
        print(total)


def get_input(file_name: str) -> list[list[str]]:
    with open(file_name, 'r') as file:
        return [[c for c in line[:-1]] for line in file.readlines()]


def main():
    file_name = 'day4.in'
    word_search = get_input(file_name)
    ws = WordSearch(word_search)
    ws.part1()
    ws.part2()


if __name__ == '__main__':
    main()
