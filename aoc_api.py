import requests
import local
import re

AOC_URL = 'https://adventofcode.com/2025/day/{}'
HEADERS = {
    'cookie': 'session={0}'.format(local.session)
}


# Fetch Puzzle Input
def get_puzzle_input(day: int, test: bool = False):
    text = read_test_data(day) if test else fetch_data(day)
    input_values = text.splitlines()
    return input_values


def read_test_data(day: int) -> str:
    return open(f'./test_data/day{day}.txt').read()


def fetch_data(day: int) -> str:
    url = AOC_URL.format(day) + '/input'
    return requests.get(url, headers=HEADERS).text


# Submit Puzzle Solution
def submit_solution(day: int, part: int, value: str) -> str:

    url = AOC_URL.format(day) + '/answer'
    response = requests.post(url, data={'level': part, 'answer': str(value)}, headers=HEADERS).text
    response = re.search(r'<main>([\S\s]*)</main>', response).group(0)
    response = re.sub(r'<(.*?)>', '', response)
    return response
