#!/usr/bin/python3
#
# https://adventofcode.com/
# 7/12/2022
#
# That made me think a little.

import json


# parse the lines of commands and outputs into a nested hash to represent the file system
# need to track the line number we are on in the list of inputs
def parse_fs( lines, dir, i = 0 ):
    while i < len(lines):
        l = lines[i]
        i+=1
        if l == "$ cd /":
            continue

        if l == "$ ls":
            # keep going until we have another cd command
            while i < len(lines) and not lines[i].startswith("$ cd"):
                if lines[i].startswith("dir "):
                    d,name = lines[i].split(" ")
                    dir[name] = { "type": "directory" }
                else:
                    s,name = lines[i].split(" ",2)
                    dir[name] = { "type": "file", "size": int(s) }
                i+=1
        elif l.startswith("$ cd"):
            p,d,name = l.split(" ")
            # return out if we are moving back up the directory
            if name == "..":
                return i
            # we need to recurse
            i = parse_fs( lines, dir[name], i )
    return i


# traverse the file system summing the file sizes at each level and adding in any directory size too
def calc_dir_size( fs ):
    size = 0
    for k in fs.keys():
        if k == "type":
            continue

        if fs[k]["type"] == "file":
            size += fs[k]["size"]
        elif fs[k]["type"] == "directory":
            size += calc_dir_size(fs[k])
    fs["size"] = size

    return size


# part 1 asked us to find directories less than a certain size and sum these sizes
def find_dirs_up_to_size( fs, lte ):
    size = 0
    for k in fs.keys():
        if k in ["size","type"]:
            continue
        if fs[k]["type"] == "directory":
            if fs[k]["size"] <= lte:
                size += fs[k]["size"]
            size += find_dirs_up_to_size( fs[k], lte )

    return size


# I thought the easist way here was to flatten the directories into an array which we can traverse for our logic
def flatten_dirs( fs ):
    dirs = []
    for k in fs.keys():
        if k in ["size","type"]:
            continue
        if fs[k]["type"] == "directory":
            dirs.append( ( k, fs[k]["size"] ) )
            dirs.extend( flatten_dirs( fs[k]) )

    return dirs


if __name__ == '__main__':
    lines = []
    with open( '7.input.txt' ) as fp:
        for line in fp:
            lines.append(line[:-1])

    # input file only contains a single "$ cd /" so no need to handle a return to root directory
    fs = {}
    parse_fs( lines, fs )
    calc_dir_size( fs )

    # print(json.dumps(fs,indent=4))

    print("1.",find_dirs_up_to_size( fs, 100000 ))

    # constants
    fs_total_size = 70000000
    fs_space_needed = 30000000

    fs_space_used = fs["size"]
    fs_space_availble = fs_total_size - fs_space_used
    need_to_free = fs_space_needed - fs_space_availble

    dirs = flatten_dirs( fs )

    # find those directories that when deleted will free enough space
    big_enough = []
    for d in dirs:
        if d[1] > need_to_free:
            big_enough.append( d)

    # find smallest from those that were big enough
    smallest = None
    for d in big_enough:
        if smallest == None or d[1] < smallest:
            smallest = d[1]

    print("2.",smallest)