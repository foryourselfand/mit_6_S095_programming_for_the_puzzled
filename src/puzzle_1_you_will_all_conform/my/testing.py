from please_conform_linear import PleaseConformLinear
from please_conform_squared import PleaseConformSquared


def main() -> None:
    # caps1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
    # caps2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']

    # solution1 = PleaseConformSquared().please_conform(caps1)
    # solution2 = PleaseConformSquared().please_conform(caps2)

    caps = ['F', 'F', 'F', 'B', 'F', 'F', 'F']
    solution = PleaseConformSquared().please_conform(caps)

    print(f'{solution=}')


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
