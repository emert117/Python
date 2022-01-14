from typing import List


def lst_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)

print(lst_avg([5, 6, 7]))