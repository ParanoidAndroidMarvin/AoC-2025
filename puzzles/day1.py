from typing import Tuple


START_VALUE = 50
MAX_VALUE = 99
MIN_VALUE = 0


def solve(puzzle_input: list[str]) -> Tuple[str, str]:
    puzzle_input = read_input(puzzle_input)
    return solve_part1(puzzle_input), solve_part2(puzzle_input)


def solve_part1 (puzzle_input: list[Tuple[str, int]]) -> str:
    count = 0
    position = START_VALUE

    for (direction, distance) in puzzle_input:
        position += distance if direction == "R" else -distance
        position %= 100

        if position == 0:
            count += 1

    return str(count)


def solve_part2 (puzzle_input: list[Tuple[str, int]]) -> str:
    count = 0
    position = START_VALUE

    for (direction, distance) in puzzle_input:
        passes, position = count_passes(position, direction, distance)
        count += passes

    return str(count)


def count_passes(position: int, direction: str, distance: int) -> Tuple[int, int]:
    count=0
    start = position

    position += distance if direction == "R" else -distance
    rotations = abs(position // 100)
    position = position % 100

    count += rotations

    if direction == "L" and (start == 0):
        count -= 1

    if (rotations == 0 or direction == "L") and position == 0:
        count += 1

    return count, position


def read_input(puzzle_input: list[str]) -> list[Tuple[str, int]]:
    return [(line[:1], int(line[1:])) for line in puzzle_input]


# I was going insane - needed to test my sanity
def assert_count_passes():
    # right
    assert count_passes(78, "R", 22) == (1, 0)
    assert count_passes(78, "R", 122) == (2, 0)
    assert count_passes(75, "R", 30) == (1, 5)
    assert count_passes(75, "R", 130) == (2, 5)
    assert count_passes(0, "R", 100) == (1, 0)
    # left
    assert count_passes(22, "L", 22) == (1, 0)
    assert count_passes(22, "L", 122) == (2, 0)
    assert count_passes(25, "L", 30) == (1, 95)
    assert count_passes(25, "L", 130) == (2, 95)
    assert count_passes(0, "L", 5) == (0, 95)


if __name__ == "__main__":
    assert_count_passes()