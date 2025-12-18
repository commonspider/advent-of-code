import math

from advent_of_code_2025.utils import Stream


def solve(problem: list[str]):
    numbers = map(int, problem[:-1])
    if problem[-1] == "+":
        return sum(numbers)
    elif problem[-1] == "*":
        return math.prod(numbers)
    else:
        raise ValueError

(
    Stream.from_input_lines()
        .map(lambda x: x.strip().split())
        .to_matrix()
        .transpose()
        .to_stream()
        .map(solve)
        .sum()
        .print()
 )
