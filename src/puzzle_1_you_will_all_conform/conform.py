# Programming for the Puzzled -- Srini Devadas
# You Will All Conform
# Input is a vector of F's and B's, in terms of forwards and backwards caps
# Output is a set of commands (printed out) to get either all F's or all B's
# Fewest commands are the goal

from collections import defaultdict
from typing import List, Tuple


def please_conform_my(caps_input: List[str]):
    caps: List[str] = caps_input.copy()

    caps.append('end')

    interval_count = defaultdict(int)
    cap_last = caps[0]

    for cap_current in caps[1:]:
        if cap_current != cap_last:
            interval_count[cap_last] += 1
            cap_last = cap_current

    interval_min = min(interval_count.items(), key=lambda item: item[1])
    cap_min = interval_min[0]

    index_start = 0
    cap_previous = caps[0]
    for index_current, cap_current in enumerate(caps[1:], 1):
        if cap_current != cap_min:
            if cap_previous == cap_min:
                index_end = index_current - 1
                if index_end == index_start:
                    print(f'Person at position {index_start} flip your cap!')
                else:
                    print(f'People in positions {index_start} through {index_end} flip your caps!')
            index_start = index_current + 1

        cap_previous = cap_current


def please_conform(caps_input: List[str]):
    caps: List[str] = caps_input.copy()

    # So we don't need to add the last interval after for loop completes execution
    caps.append('end')

    intervals: List[Tuple[int, int, str]] = list()
    count_forward: int = 0
    count_backward: int = 0
    index_previous: int = 0

    # Determine intervals where caps are on in the same direction
    for index_current in range(1, len(caps)):
        if caps[index_previous] != caps[index_current]:
            intervals.append((index_previous, index_current - 1, caps[index_previous]))

            if caps[index_previous] == 'F':
                count_forward += 1
            else:
                count_backward += 1
            index_previous = index_current

    if count_forward < count_backward:
        cap_to_flip = 'F'
    else:
        cap_to_flip = 'B'

    for interval in intervals:
        cap_current = interval[2]
        if cap_current == cap_to_flip:
            if interval[0] == interval[1]:
                print('Person at position', interval[0], 'flip your cap!')
            else:
                print('People in positions', interval[0], 'through', interval[1], 'flip your caps!')


def please_conform_one_pass(caps_input: List[str]):
    caps: List[str] = caps_input.copy()

    caps = caps + [caps[0]]
    for i in range(1, len(caps)):
        if caps[i] != caps[i - 1]:
            if caps[i] != caps[0]:
                print('People in positions', i, end='')
            else:
                print(' through', i - 1, 'flip your caps!')


def solution_print(pleaseConformFunction, *caps: List[str]):
    print(pleaseConformFunction.__name__)
    print()
    for cap in caps:
        print(*cap)
        pleaseConformFunction(cap)
        print()
    print('-' * 50)


def main() -> None:
    caps1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
    caps2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']

    caps = caps1, caps2

    solution_print(please_conform_my, *caps)
    solution_print(please_conform, *caps)
    solution_print(please_conform_one_pass, *caps)


if __name__ == '__main__':
    main()

# when there is only one cap type input is already result
# input: F
# input: B
# input: F F
# input: B B B
# input: F F F F F
# result: ready

# where is the same number of F's and B's intervals result don't matter because requests number will be the same
# input: F B
# input: B F
# input: F F B B
# input: B B B F F F
# input: F B F B
# input: B F B F
# result: either F or B

# input F B F
# result: B

# we optimizing solution for coach, not for player. so minimizing requests is goal, not minimizing peoples movement
# input: F F F B F F F
# result: B

# input: F B F B
# result: either F or B

# input: F B F B F
# result: B

# input: F B B B F B B B F
# result: B

# so conclusion of small analysis: we can flip starting from second interval: it always be the answer

# interval count: result
# 1: ready
# even: F or B
# odd: second interval
