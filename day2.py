#!/usr/bin/python3
#
# https://adventofcode.com/
# 1/12/2022
#
# My head is full of cold! Feel like I knifed and forked it.
#
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
#
# Points:
# 1 for Rock, 2 for Paper, and 3 for Scissors
#
# Outcome scores:
# 0 loose, 3 draw, and 6 for the win


points1 = {
    "X":1,
    "Y":2,
    "Z":3
}
points2 = {
    "A":1,
    "B":2,
    "C":3
}

if __name__ == '__main__':
    score = 0
    # Play RPS with the two moves and calculate the outcome, adding scores as you go.
    with open( '2.input.txt' ) as fp:
        for line in fp:
            (a,b) = line[:-1].split(" ")
            s1 = points1[b]
            # draws
            if (a == "A" and b == "X") or (a == "B" and b == "Y") or (a == "C" and b == "Z"):
                score += (s1 + 3)
            # wins
            elif (a == "A" and b == "Y") or (a == "B" and b == "Z") or (a == "C" and b == "X"):
                score += (s1 + 6)
            # loose
            elif (a == "A" and b == "Z") or (a == "B" and b == "X") or (a == "C" and b == "Y"):
                score += (s1 + 0)

    print("1. ",score)

    # Now X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
    # Calculate the move to meet the goal and add up the scores.
    score = 0
    with open( '2.input.txt' ) as fp:
        for line in fp:
            (a,b) = line[:-1].split(" ")

            # draw
            if (b == "Y"):
                score += (3 + points2[a])
            # win
            elif (b == "Z"):
                p = 0
                if (a == "A"):
                    p = points2["B"]
                elif (a == "B"):
                    p = points2["C"]
                elif (a == "C"):
                    p = points2["A"]
                score += (6 + p)
            # loose
            elif (b == "X"):
                p = 0
                if (a == "A"):
                    p = points2["C"]
                elif (a == "B"):
                    p = points2["A"]
                elif (a == "C"):
                    p = points2["B"]
                score += (0 + p)

    print("2. ",score)
