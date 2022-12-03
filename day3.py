#!/usr/bin/python3
#
# https://adventofcode.com/
# 3/12/2022
#
# Head still full of cold! Pleased with the way this solution flowed easily.

# calculate the score based on an array of common characters
def get_score( common ):
    score = 0
    for c in common:
        if c >= "a" and c <= "z":
            score += ( ord(c) - ord("a") + 1 )
        else:
            score += ( ord(c) - ord("A") + 27 )
    return score


# look for the common characters across three sets
def find_common( group ):
    r1 = [ch for ch in group[0]]
    r2 = [ch for ch in group[1]]
    r3 = [ch for ch in group[2]]
    return list(set(r1) & set(r2) & set(r3))


if __name__ == '__main__':
    score = 0
    common = []
    # split lines in half and look for the common character using logical AND on two arrays
    with open( '3.input.txt' ) as fp:
        for line in fp:
            line = line[:-1]
            l = int(len(line)/2)
            r1 = [ch for ch in line[0:l]]
            r2 = [ch for ch in line[l:]]

            common.extend( list(set(r1) & set(r2)) )

    print("1. ",get_score(common))

    score = 0
    common = []
    # take three lines at a time and look for the common character across the three lines.
    with open( '3.input.txt' ) as fp:
        group = []
        for line in fp:
            line = line[:-1]
            if len(group) < 3:
                group.append(line)
            else:
                common.extend(find_common( group ))
                group.clear()
                group.append(line)
        # this is for last line in file
        common.extend(find_common( group ))

    print("2. ",get_score(common))
