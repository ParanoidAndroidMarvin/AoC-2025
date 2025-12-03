from typing import Tuple


def solve(puzzle_input: list[str]) -> Tuple[str, str]:
    battery_banks = [[int(battery) for battery in list(bank)] for bank in puzzle_input]
    return solve_part1(battery_banks), solve_part2(battery_banks)


def solve_part1(battery_banks: list[list[int]]) -> str:
    total_power = 0
    for bank in battery_banks:
        total_power += _get_max_power(bank)
    return str(total_power)


def solve_part2(battery_banks: list[list[int]]) -> str:
    total_power = 0
    for bank in battery_banks:
        total_power += _get_max_power2(bank)
    return str(total_power)


def _get_max_power(bank: list[int]) -> int:
    largest_battery = max(bank)
    largest_battery_position = bank.index(largest_battery)
    largest_battery_is_last = largest_battery_position == len(bank) - 1
    second_largest_battery = max(bank[:-1] if largest_battery_is_last else bank[largest_battery_position + 1:])

    if largest_battery_is_last:
        return 10 * second_largest_battery + largest_battery
    return 10 * largest_battery + second_largest_battery


def _get_max_power2(bank: list[int]) -> int:
    if len(bank) <= 12:
        return int(''.join(map(str,bank)))

    max_power = 0
    for i, _ in enumerate(bank):
        bank_copy = bank.copy()
        bank_copy.pop(i)
        power = int(''.join(map(str,bank_copy)))
        if power > max_power:
            max_power = power
    return _get_max_power2(list(map(int, str(max_power))))
