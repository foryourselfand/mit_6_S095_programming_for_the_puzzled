from typing import List

from structures import Interval


class SolutionPleaseConform:
    def please_conform(self, caps: List[str]) -> List[Interval]:
        caps: List[str] = caps.copy()

        caps.append('end')

        interval_inputs: List[Interval] = list()
        count_forward: int = 0
        count_backward: int = 0
        index_previous: int = 0

        for index_current in range(1, len(caps)):
            cap_current = caps[index_current]
            cap_previous = caps[index_previous]

            if cap_current != cap_previous:
                interval_input = Interval(start=index_previous,
                                          end=index_current - 1,
                                          cap_type=cap_previous)
                interval_inputs.append(interval_input)

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

        interval_results: List[Interval] = list()

        for interval_input in interval_inputs:
            if interval_input.cap_type == cap_to_flip:
                interval_result: Interval = interval_input
                interval_results.append(interval_result)

        return interval_results


def main() -> None:
    caps1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
    caps2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']

    caps = caps1, caps2

    solution1 = SolutionPleaseConform().please_conform(caps1)
    solution2 = SolutionPleaseConform().please_conform(caps2)

    print(f'{solution1=}')
    print(f'{solution2=}')

    # solution_print(please_conform_my_old, *caps)
    # solution_print(please_conform, *caps)
    # solution_print(please_conform_one_pass, *caps)


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
