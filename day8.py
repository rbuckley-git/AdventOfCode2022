#!/usr/bin/python3
#
# https://adventofcode.com/
# 8/12/2022
#
# Nice little grid problem. 
# Tried to think about a more generic way of looking in each direction but ended up just knife and forking it to get the answer.
# Cold almost completely gone now.

import json

def tree_visible_left_to_right( grid, tree ):
    highest = grid[tree]

    x,y = tree
    while x > 0:
        x-=1
        if grid[(x,y)] >= highest:
            return False

    return True

def tree_visible_right_to_left( grid, tree, max_x ):
    highest = grid[tree]

    x,y = tree
    while x < max_x-1:
        x+=1
        if grid[(x,y)] >= highest:
            return False

    return True


def tree_visible_top_to_bottom( grid, tree ):
    highest = grid[tree]

    x,y = tree
    while y > 0:
        y-=1
        if grid[(x,y)] >= highest:
            return False

    return True


def tree_visible_bottom_to_top( grid, tree, max_y ):
    highest = grid[tree]

    x,y = tree
    while y < max_y-1:
        y+=1
        if grid[(x,y)] >= highest:
            return False

    return True


def tree_visible( grid, tree, max_x, max_y ):
    if tree_visible_left_to_right( grid, tree ):
        return True
    if tree_visible_right_to_left( grid, tree, max_x ):
        return True
    if tree_visible_top_to_bottom( grid, tree ):
        return True
    if tree_visible_bottom_to_top( grid, tree, max_y ):
        return True

def calc_scenic_score(grid, tree, max_x,max_y):
    height = grid[tree]
    score = 1
    # left
    x,y = tree
    viewing_distance = 0
    while x > 0:
        viewing_distance+=1
        x-=1
        if grid[(x,y)] >= height:
            break
    score *= viewing_distance
    # right
    x,y = tree
    viewing_distance = 0
    while x < max_x-1:
        viewing_distance+=1
        x+=1
        if grid[(x,y)] >= height:
            break
    score *= viewing_distance
    # up
    x,y = tree
    viewing_distance = 0
    while y > 0:
        viewing_distance+=1
        y-=1
        if grid[(x,y)] >= height:
            break
    score *= viewing_distance
    # down
    x,y = tree
    viewing_distance = 0
    while y < max_y-1:
        viewing_distance+=1
        y+=1
        if grid[(x,y)] >= height:
            break
    score *= viewing_distance

    return score


if __name__ == '__main__':
    grid = {}
    y = 0
    with open( '8.input.txt' ) as fp:
        for line in fp:
            x = 0
            for ch in line[:-1]:
                grid[(x,y)] = int(ch)
                x+=1
            y+=1
    max_x = x
    max_y = y

    visible = set()
    for tree in grid:
        if tree_visible(grid,tree,max_x,max_y):
            visible.add(tree)
    print("1.",len(visible))

    scenic_score = 0
    for tree in grid:
        scenic_score = max(calc_scenic_score(grid,tree,max_x,max_y), scenic_score)
    print("2.",scenic_score)
