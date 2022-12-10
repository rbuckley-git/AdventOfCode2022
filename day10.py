#!/usr/bin/python3
#
# https://adventofcode.com/
# 10/12/2022
#
# Nice and straightforward. Had to break to make pizza between parts. Trick was making the X_register observation at the right part in the cycle.

import json

# reference constants
cycles = {
    "noop": 1,
    "addx": 2
}

if __name__ == '__main__':
    instructions = []
    with open( '10.input.txt' ) as fp:
        for line in fp:
            line = line[:-1]
            if len(line.split(" ")) == 1:
                instructions.append({"code":line})
            else:
                ins,arg = line.split(" ")
                instructions.append({"code":ins,"arg":int(arg)})

    # set things up for the first cycle
    part1_strength = 0
    ins = 0
    X_register = 1
    opcode = instructions[ins]
    instruction_cycle = cycles[opcode["code"]]
    line = ""
    part2_lines = []
    crt_x = 0

    # setup a loop for the number of iterations we need for the puzzle
    for i in range(1,241):
        if instruction_cycle == 0:
            ins+=1
            if ins >= len(instructions):
                print("out of code after",ins)
                break
            opcode = instructions[ins]
            instruction_cycle = cycles[opcode["code"]]

        # calculate answer for part 1
        if i in [20,60,100,140,180,220]:
            part1_strength += (i * X_register)

        # CRT position crt_x is checked against the 3 character sprite with a picrt_xel being displayed if there is a match
        if crt_x in [X_register-1,X_register,X_register+1]:
            line = line + "*"
        else:
            line = line + " "

        # increment the CRT position printing and wrapping at 40 characters
        crt_x += 1
        if len(line) == 40:
            part2_lines.append(line)
            line = ""
            crt_x = 0

        # at the end of the cycle, change the X_register register
        instruction_cycle-=1
        if instruction_cycle == 0:
            if "arg" in opcode:
                X_register+=opcode["arg"] 

    print("1.",part1_strength)
    print("2. Captial letters displayed below on the CRT")
    for line in part2_lines:
        print(line)
