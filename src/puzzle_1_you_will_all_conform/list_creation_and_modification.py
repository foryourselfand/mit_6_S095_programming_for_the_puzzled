def listConcatenate(caps):
    caps = caps + ['END']
    print(caps)


capA = ['F', 'F', 'B']
listConcatenate(capA)
print(capA)


def listAppend(caps):
    caps.append('END')
    print(caps)


capA = ['F', 'F', 'B']
listAppend(capA)
print(capA)
