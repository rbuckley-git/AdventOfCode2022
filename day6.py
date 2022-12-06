#!/usr/bin/python3
#
# https://adventofcode.com/
# 6/12/2022
#
# Easy look for number of unit characters in a set. Refactored solution a little following completion of the problem.

def get_marker_position( s, marker_length ):
    buffer = []
    for i in range(0,len(s)):
        # add character onto buffer popping first one out if length is greater than we are looking for. 
        buffer.append(s[i])
        if len(buffer)>marker_length:
            buffer.pop(0)

        if marker_length == len(set(buffer)):
            return i+1


if __name__ == '__main__':
    seq = ""
    with open( '6.input.txt' ) as fp:
        for line in fp:
            seq = line[:-1]

    print("1.",get_marker_position(seq,4))
    print("2.",get_marker_position(seq,14))