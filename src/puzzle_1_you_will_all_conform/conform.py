# Programming for the Puzzled -- Srini Devadas
# You Will All Conform
# Input is a vector of F's and B's, in terms of forwards and backwards caps
# Output is a set of commands (printed out) to get either all F's or all B's
# Fewest commands are the goal

from collections import defaultdict


def pleaseConformMy(caps):
    caps.append('end')
    
    interval_count = defaultdict(int)
    cap_last = caps[0]
    
    for cap_current in caps[1:]:
        if cap_current != cap_last:
            interval_count[cap_last] += 1
            cap_last = cap_current
    
    interval_min = min(interval_count.items(), key = lambda item: item[1])
    cap_min = interval_min[0]
    
    index_start = 0
    cap_previous = caps[0]
    for index_current, cap_current in enumerate(caps[1:], 1):
        if cap_current != cap_min:
            if cap_previous == cap_min:
                index_end = index_current - 1
                print(f'People in positions {index_start} through {index_end} flip your caps!')
            index_start = index_current + 1
        
        cap_previous = cap_current
    print()


def pleaseConform(caps):
    # Initialization
    start = 0
    forward = 0
    backward = 0
    intervals = []
    
    # Determine intervals where caps are on in the same direction
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            # each interval is a tuple with 3 elements (start, end, type)
            intervals.append((start, i - 1, caps[start]))
            
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i
    
    # Need to add the last interval after for loop completes execution
    intervals.append((start, len(caps) - 1, caps[start]))
    if caps[start] == 'F':
        forward += 1
    else:
        backward += 1
    
    ##    print (intervals)
    ##    print (forward, backward)
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == flip:
            # Exercise: if t[0] == t[1] change the printing!
            print('People in positions', t[0],
                  'through', t[1], 'flip your caps!')


def pleaseConformOpt(caps):
    # Initialization
    start = 0
    forward = 0
    backward = 0
    intervals = []
    
    caps = caps + ['END']
    
    # Determine intervals where caps are on in the same direction
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            # each interval is a tuple with 3 elements (start, end, type)
            intervals.append((start, i - 1, caps[start]))
            
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i
    
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == flip:
            # Exercise: if t[0] == t[1] change the printing!
            print('People in positions', t[0], 'through', t[1], 'flip your caps!')


def pleaseConformOnepass(caps):
    caps = caps + [caps[0]]
    for i in range(1, len(caps)):
        if caps[i] != caps[i - 1]:
            if caps[i] != caps[0]:
                print('People in positions', i, end = '')
            else:
                print(' through', i - 1, 'flip your caps!')


def pleaseConformExercise(caps):
    # Initialization
    start = 0
    forward = 0
    backward = 0
    intervals = []
    
    # Determine intervals where caps are on in the same direction
    for i in range(len(caps)):
        if caps[start] != caps[i]:
            # each interval is a tuple with 3 elements (start, end, type)
            intervals.append((start, i - 1, caps[start]))
            
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i
    
    # Need to add the last interval after for loop completes execution
    intervals.append((start, len(caps) - 1, caps[start]))
    if caps[start] == 'F':
        forward += 1
    else:
        backward += 1
    
    ##    print (intervals)
    ##    print (forward, backward)
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == flip:
            # Exercise: if t[0] == t[1] change the printing!
            if t[0] == t[1]:
                print('Person at position', t[0], 'flip your cap!')
            else:
                print('People in positions', t[0], 'through', t[1], 'flip your caps!')


def main() -> None:
    caps1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
    caps2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']
    
    pleaseConform(caps1)
    pleaseConform(caps2)


if __name__ == '__main__':
    main()
