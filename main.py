import curses
import time
from typing import Tuple

import aoc_api
from puzzles import day1, day2, day3

selected_day = 1
solution: Tuple[str, str] | None = None
in_menu = True

puzzles = {
    "Secret Entrance": day1.solve,
    "Gift Shop": day2.solve,
    "Lobby": day3.solve
}


def draw_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Advent of Code - 2025")
    stdscr.addstr(1, 0, "=================")
    stdscr.addstr(3, 0, "Choose puzzle:")

    for i, name in enumerate(puzzles.keys(), start=1):
        selector = ">" if selected_day == i else " "
        endsel = "<" if selected_day == i else " "
        stdscr.addstr(4 + i, 0, f"{selector} Day {i}: {name} {endsel}")

    stdscr.addstr(
        6 + len(puzzles),
        0,
        "[↑]Up [↓]Down [↩]Run [T]Test [Esc]Exit",
        )
    stdscr.refresh()


def navigate(direction):
    global selected_day
    selected_day += direction
    if selected_day < 1:
        selected_day = len(puzzles)
    elif selected_day > len(puzzles):
        selected_day = 1


def draw_run_result(stdscr, test=False):
    stdscr.clear()
    mode = "[TEST] " if test else ""
    stdscr.addstr(0, 0, f"{mode}Puzzle result day {selected_day}:")
    stdscr.addstr(1, 0, "--------------------------------------")

    try:
        global solution
        puzzle_input = aoc_api.get_puzzle_input(selected_day, test)
        solver = list(puzzles.values())[selected_day - 1]

        start = time.time()
        solution = solver(puzzle_input)
        stop = time.time()

        stdscr.addstr(3, 0, f"Solution 1: {solution[0]}")
        stdscr.addstr(4, 0, f"Solution 2: {solution[1]}")
        stdscr.addstr(6, 0, f"Execution time: {round(stop - start, 3)}s")

    except FileNotFoundError:
        stdscr.addstr(3, 0, f"No test data found for day {selected_day}!")

    if test:
        stdscr.addstr(8, 0, "[Backspace] Menu  [Esc] Exit")
    else:
        stdscr.addstr(
            8,
            0,
            "[Backspace]Menu   [1]Submit Part 1   [2]Submit Part 2   [Esc]Exit",
        )

    stdscr.refresh()


def draw_submit(stdscr, part):
    global solution
    stdscr.clear()
    if not solution:
        stdscr.addstr(0, 0, "No solution available to submit.")
    else:
        res = aoc_api.submit_solution(selected_day, part, solution[part - 1])
        stdscr.addstr(0, 0, res)

    stdscr.addstr(2, 0, "[Backspace]Menu  [Esc]Exit")
    stdscr.refresh()


def main(stdscr):
    global in_menu

    curses.curs_set(0)  # hide cursor
    stdscr.nodelay(False)
    stdscr.keypad(True)

    draw_menu(stdscr)

    while True:
        key = stdscr.getch()

        # ESC exits everywhere
        if key == 27:
            break

        if in_menu:
            if key in (curses.KEY_UP, curses.KEY_LEFT):
                navigate(-1)
                draw_menu(stdscr)

            elif key in (curses.KEY_DOWN, curses.KEY_RIGHT):
                navigate(1)
                draw_menu(stdscr)

            elif key in (curses.KEY_ENTER, 10, 13):  # Enter
                in_menu = False
                draw_run_result(stdscr)

            elif key in (ord("t"), ord("T")):
                in_menu = False
                draw_run_result(stdscr, test=True)

        else:
            # In the results screen
            if key == curses.KEY_BACKSPACE or key == 127:
                in_menu = True
                draw_menu(stdscr)

            elif key == ord("1"):
                draw_submit(stdscr, 1)

            elif key == ord("2"):
                draw_submit(stdscr, 2)

    # exit: restore terminal
    stdscr.clear()
    stdscr.refresh()


if __name__ == "__main__":
    curses.wrapper(main)
