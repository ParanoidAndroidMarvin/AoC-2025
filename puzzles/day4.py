from typing import Tuple

import numpy as np
from numpy.typing import NDArray


PAPER = '@'
EMPTY = '.'


def solve(puzzle_input: list[str]) -> Tuple[str, str]:
    warehouse_map = np.array([list(line) for line in puzzle_input], str)
    return _solve(warehouse_map), _solve(warehouse_map, True)


def _solve(warehouse_map: NDArray[np.str_], remove_papers: bool = False, retrieved_papers: int = 0) -> str:
    start = retrieved_papers
    new_warehouse_map = np.copy(warehouse_map)

    rows, cols = warehouse_map.shape
    for x, y in np.ndindex((rows, cols)):
        if warehouse_map[x, y] != PAPER:
            continue
        area = warehouse_map[max(0, x-1):min(rows, x+2), max(0, y-1):min(cols, y+2)]
        paper_in_area = np.count_nonzero(area == PAPER)
        if paper_in_area <= 4:
            retrieved_papers += 1
            new_warehouse_map[x, y] = EMPTY

    if remove_papers and start != retrieved_papers:
        return _solve(new_warehouse_map, remove_papers, retrieved_papers)
    return str(retrieved_papers)