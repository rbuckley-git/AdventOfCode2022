#!/usr/bin/python3
#
# https://adventofcode.com/
# 5/12/2022
#
# Getting over cold. Slight cough remains.
# Nice little parsing challenge this with some list manipulation. As always, once the data is in the right format, it is easy.

import copy

# used twice, take append the last block from each stack in turn
def calc_code( stacks ):
    code = ""
    for s in stacks:
        code = code + s[-1]
    return code


# for debugging
def print_stacks( stacks ):
    for sl in stacks:
        print(sl)


if __name__ == '__main__':
    stacks = []
    instructions = []

    # annoyingly the initial state is nice visually but useless for parsing so capture all the lines up to the empty line then reverse them.
    # take a record of each of the instruction lines for later
    with open( '5.input.txt' ) as fp:
        stack_lines = []
        stack_lines_complete = False
        for line in fp:
            line = line[:-1]
            
            if line == "":
                stack_lines_complete = True
            
            if not stack_lines_complete:
                stack_lines.append( line )
            elif line.startswith("move"):
                instructions.append( line )
        
        # now reverse the stack to make it easier to parse
        stack_lines.reverse()

        # get maximum stack line from the first line to setup our list of lists
        max_stack = max([int(x) for x in stack_lines[0].split("   ")])
        for j in range(0,max_stack):
            stacks.append([])

    # bit of positional sums to get the character in each stack if any and add them to the appropriate list.
    for i in range(1,len(stack_lines)):
        sl = stack_lines[i]
        for j in range(0,max_stack):
            ch = sl[1+j*4:2+j*4]
            if ch != " ":
                stacks[j].append(ch)

    # stacks all initialised and ready for the crane moves

    # take a copy of the initial state so we can reuse in part 2.
    stacks_copy = copy.deepcopy(stacks)

    for ins in instructions:
        words = ins.split(" ")
        q,s,d = [int(x) for x in [words[1],words[3],words[5]]]
        # part 1, one block at a time
        for j in range(0,q):
            pick_up = stacks[s-1][-1]
            stacks[s-1].pop(-1)
            stacks[d-1].append(pick_up)

    print("1.",calc_code(stacks))

    # restore copy
    stacks = copy.deepcopy(stacks_copy)
 
    for ins in instructions:
        words = ins.split(" ")
        q,s,d = [int(x) for x in [words[1],words[3],words[5]]]
        # part 2, q blocks at a time
        pick_up = stacks[s-1][q*-1:]
        stacks[d-1].extend(pick_up)
        for j in range(0,q):
            stacks[s-1].pop(-1)

    print("2.",calc_code(stacks))
