#!/usr/bin/env python2
def islands(sea):
    sea = '0%s0' % sea
    difn = 0
    for i in range(0,len(sea)):
        curr = sea[i]
        if curr != '1':
            continue
        try:
            next = sea[i + 1]
        except IndexError:
            next = curr
        if curr != next:
            difn += 1
    return difn

s='00000000111111100110101111100011111001'
print islands(s)
