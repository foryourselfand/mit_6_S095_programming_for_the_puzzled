from typing import Callable, List, NamedTuple


class Interval(NamedTuple):
    start: int
    end: int
    cap_type: str


def please_conform(caps: List[str]):
    caps: List[str] = caps.copy()

    caps.append('end')

    intervals: List[Interval] = list()
    count_forward: int = 0
    count_backward: int = 0
    index_previous: int = 0

    for index_current in range(1, len(caps)):
        cap_current = caps[index_current]
        cap_previous = caps[index_previous]

        if cap_current != cap_previous:
            interval = Interval(start=index_previous,
                                end=index_current - 1,
                                cap_type=cap_previous)
            intervals.append(interval)

            if cap_previous == 'F':
                count_forward += 1
            else:
                count_backward += 1
            index_previous = index_current

    cap_to_flip: str
    if count_forward < count_backward:
        cap_to_flip = 'F'
    else:
        cap_to_flip = 'B'

    for interval in intervals:
        if interval.cap_type == cap_to_flip:
            if interval.start == interval.end:
                print('Person at position', interval.start, 'flip your cap!')
            else:
                print('People in positions', interval.start, 'through', interval.end, 'flip your caps!')


def please_conform_one_pass(caps: List[str]):
    caps: List[str] = caps.copy()

    cap_first: str = caps[0]
    caps.append(cap_first)

    interval_start: int = 0
    for index_current in range(1, len(caps)):
        index_previous = index_current - 1

        cap_current: str = caps[index_current]
        cap_previous: str = caps[index_previous]

        if cap_current != cap_previous:
            if cap_current != cap_first:
                interval_start = index_current
            else:
                if index_previous == interval_start:
                    print('Person at position', index_previous, 'flip your cap!')
                else:
                    print('People in positions', interval_start, 'through', index_previous, 'flip your caps!')


def solution_print(please_conform_function: Callable, *caps: List[str]):
    print(please_conform_function.__name__)
    for cap in caps:
        print()
        print(*cap)
        please_conform_function(cap)
    print('-' * 50)


def main() -> None:
    caps1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
    caps2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']

    caps = caps1, caps2

    # solution_print(please_conform_my_old, *caps)
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

# TODO: functions with solutions dont print out solutions, but just returning special structure
# TODO: tests for solution functions
