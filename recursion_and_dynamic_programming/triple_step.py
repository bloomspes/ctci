from typing import List


def triple_step(n, memo: List[int]) -> List[int]:

    step = []

    if n == 0 or n == 1 or n == 2:
        step.append(1)
        return step[n]
    else:
        step.append(triple_step(n-1) + triple_step(n-2))
        return step[n]
