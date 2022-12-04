#!/usr/bin/python3
#
# https://adventofcode.com/
# 4/12/2022
#
# Head still full of cold! Took a detour comparing strings rather than ints. Might have been quicker creating sets and doing 
# set arithmetric but hey ho!

if __name__ == '__main__':
    contained_within = 0
    overlaps = 0    
    with open( '4.input.txt' ) as fp:
        for line in fp:
            (r1,r2) = line[:-1].split(",")
            (a1,a2) = [int(x) for x in r1.split("-")]
            (b1,b2) = [int(x) for x in r2.split("-")]

            if (a1 >= b1 and a2 <= b2) or ( a2 >= b2 and a1 <= b1):
                contained_within+=1

            if (b1 <= a1 and b2 >= a1) or (b1 <= a2 and b2 >= a2 ) or (a1 <= b1 and a2 >= b1) or (a1 <= b2 and a2 >= b2):
                overlaps+=1

    print("1.",contained_within)
    print("2.",overlaps)
