from typing import Tuple

SPLIT_LINE = ""

def solve(puzzle_input: list[str]) -> Tuple[str, str]:
    split_idx = puzzle_input.index(SPLIT_LINE)
    fresh_id_ranges: list[Tuple[int, int]] = [(int(start), int(end)) for line in puzzle_input[:split_idx] for start, end in [line.split("-")]]
    ids = list(map(int, puzzle_input[split_idx + 1:]))
    return solve_part1(fresh_id_ranges, ids), solve_part2(fresh_id_ranges)


def solve_part1(fresh_id_ranges: list[Tuple[int, int]], ids: list[int]) -> str:
    fresh_ids = [x for x in ids if any(1 for start, end in fresh_id_ranges if start <= x <= end)]
    return str(len(fresh_ids))


def solve_part2(fresh_id_ranges: list[Tuple[int, int]]) -> str:
    fresh_id_ranges.sort(key = lambda x: x[0])
    merged_fresh_id_ranges = [fresh_id_ranges[0]]
    for start, end in fresh_id_ranges:
        last_start, last_end = merged_fresh_id_ranges[-1]

        if start <= last_end:
            merged_fresh_id_ranges[-1] = (last_start, max(last_end, end))
        else:
            merged_fresh_id_ranges.append((start, end))

    return str(sum([end - start + 1 for start, end in merged_fresh_id_ranges]))