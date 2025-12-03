import re
from typing import Tuple


def solve(puzzle_input: list[str]) -> Tuple[str, str]:
    ranges = _get_ranges(puzzle_input)
    return _solve_part1(ranges), _solve_part2(ranges)


def _get_ranges(puzzle_input: list[str]) -> list[Tuple[int, int]]:
    return [(int(start), int(end)) for line in puzzle_input[0].split(",") for start, end in [line.split("-")]]


def _solve_part1(ranges: list[Tuple[int, int]]) -> str:
    invalid_ids: list[int] = []
    for start, end in ranges:
        even_ids = [x for x in range(start, end + 1) if not len(str(x)) % 2]
        invalid_ids += [int(x) for x in even_ids if str(x).startswith(str(x)[len(str(x))//2:])]

    return str(sum(invalid_ids))


def _solve_part2(ranges):
    invalid_ids: list[int] = []
    regex = re.compile(r"^(.+)(\1+)$")
    for start, end in ranges:
        ids = range(start, end + 1)
        invalid_ids += [x for x in ids if regex.match(str(x))]

    return str(sum(invalid_ids))