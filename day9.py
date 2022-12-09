#!/usr/bin/python3
#
# https://adventofcode.com/
# 9/12/2022
#
# That was a little bugger. Algorithm for part 1 did not work for part 2 as it did not deal with abs 2,2 separation. Took a while to debug.

import json

moves = {
    "R": (1,0),
    "L": (-1,0),
    "U": (0,1),
    "D": (0,-1),
}

def move_tail(H,T):
    D = (H[0]-T[0],H[1]-T[1])
    if abs(D[0]) == 2 and abs(D[1]) == 2:
        T = (T[0]+D[0]/2,T[1]+D[1]/2)
        return T

    if abs(D[1]) == 2:
        T = (T[0]+D[0],T[1])
    elif abs(D[0]) == 2:
        T = (T[0],T[1]+D[1])
    if D[0] > 1:
        T = (T[0]+1,T[1])
    elif D[0] < -1:
        T = (T[0]-1,T[1])
    if D[1] > 1:
        T = (T[0],T[1]+1)
    elif D[1] < -1:
        T = (T[0],T[1]-1)
    return T

def part1( instructions ):
    s = (0,0)
    H = s
    T = s
    visits = set()
    for ins in instructions:
        move = moves[ins[0]]
        for i in range(ins[1]):
            H = (H[0]+move[0],H[1]+move[1])
            T = move_tail(H,T)
            visits.add(T)
    return len(visits)


def print_grid(H):
    for y in range(15,-15,-1):
        line = ""
        for x in range(-15,15):
            ch = "."
            for h in range(len(H)):
                if (x,y) == H[h]:
                    ch = str(h)
                    break
            line = line + ch
        print(line)
    print()


def part2( instructions ):
    s = (0,0)
    H = []
    for i in range(10):
        H.append(s)
    
    visits = set()
    for ins in instructions:
        move = moves[ins[0]]
        for i in range(ins[1]):
            # move the first in the chain
            H[0] = (H[0][0]+move[0],H[0][1]+move[1])
            # then iterate through the rest of the chain moving them along relative to the first
            for h in range(1,len(H)):
                H[h] = move_tail(H[h-1],H[h])
            visits.add(H[9])
        # print_grid(H)
    return len(visits)


if __name__ == '__main__':
    instructions = []
    with open( '9.input.txt' ) as fp:
        for line in fp:
            d,n = line[:-1].split(" ")
            n = int(n)
            instructions.append((d,n))

    print("1.",part1(instructions))
    print("2.",part2(instructions))
