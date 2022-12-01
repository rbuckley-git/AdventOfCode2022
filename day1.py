#!/usr/bin/python3
#
# https://adventofcode.com/
# 1/12/2022
#
# Straightforward enough.
#

if __name__ == '__main__':
    elves = []
    with open( '1.input.txt' ) as fp:
        cal = 0
        for line in fp:
            line = line[:-1]
            if line == "":
                elves.append( cal )
                cal = 0
                continue
            cal += int( line )

    elves.sort()
    print("1. ",elves[-1])
    print("2. ",sum(elves[-3:]))
