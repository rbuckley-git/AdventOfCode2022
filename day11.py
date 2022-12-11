#!/usr/bin/python3
#
# https://adventofcode.com/
# 11/12/2022
#
# First part of this was straightforward. Some parsing into an array of Monkey objects. Follow the rules and get the answer out.
# It had snowed here overnight and throughout the day, so spent a lot of time outside with the kids building snowmen and sleging. 
# Part 2 was hard and clear it is one of those problems where a clever optimisation was needed. Could not work out using the usual 
# patterns. Had to resort to external assistance on this part, the first time this year.
# So the trick is to constrain the values as they get very large very quickly. If they are constrained to the modulus of the 
# product of the unique divisors in the problem, this calculates quickly as the maths is kept small.
# So I claim part 1 as my own but part 2 is understood with external input.

import json
import re
import copy

class Monkey:
    id: None
    items = None
    operation = None
    divisor = None
    true_throw = None
    false_throw = None
    inspection_count = 0
    multiple_of_divisors = None

    def __init__(self, id):
        self.id = id

    def __str__(self) -> str:
        s = {
            "id": self.id,
            "items": self.items,
            "count": self.inspection_count
        }
        return str(s)
    
    # return (destination monkey, new worry)
    def throw_item(self):
        if len(self.items) == 0:
            return None

        worry = self.items.pop(0)
        self.inspection_count += 1
        worry = self.calc_operation(worry)

        if worry % self.divisor == 0:
            return (self.true_throw,worry)

        return (self.false_throw,worry)
        
    def calc_operation(self,worry):
        old = worry
        worry = eval(self.operation)
        # part 1 worry is divided by 3 each time to keep the numbers constrained
        if self.multiple_of_divisors == None:
            worry = worry // 3
        # part 2 optimisation to keep the numbers managable, only interested in the modulus
        if self.multiple_of_divisors:
            worry = worry % self.multiple_of_divisors
        return worry


def calc_monkey_business( monkeys ):
    inspections = [m.inspection_count for m in monkeys]
    inspections.sort()
    inspections.reverse()

    return inspections[0] * inspections[1]


def calc_multiple_of_divisors( monkeys ):
    divisors = set()
    for x in [m.divisor for m in monkeys]:
        divisors.add( x )

    product = 1
    for d in divisors:
        product *= d
    
    return product

# play a given number of rounds, returning the monkey business value
def play( monkeys, rounds ):
    for round in range(rounds):
        for m in monkeys:
            while True:
                t = m.throw_item()
                if t == None:
                    break
                d,w = t
                monkeys[d].items.append(w)

    return calc_monkey_business( monkeys )


def set_multiple_of_divisors( monkeys ):
    multiple_of_divisors = calc_multiple_of_divisors( monkeys )
    for m in monkeys:
        m.multiple_of_divisors = multiple_of_divisors

if __name__ == '__main__':
    monkeys = []
    with open( '11.input.txt' ) as fp:
        monkey = None
        for line in fp:
            line = line[:-1]
            if line == "":
                monkeys.append( monkey )

            is_monkey = re.match("^Monkey\s(\d+):",line)
            if is_monkey:
                id = int(is_monkey.groups(1)[0])
                monkey = Monkey(id)

            is_starting_items = re.match("^\s+Starting\sitems:\s([\d,\s]+)",line)
            if is_starting_items:
                si = is_starting_items.groups(1)[0]
                monkey.items = [int(x) for x in si.split(", ")]

            is_operation = re.match("^\s+Operation:\snew\s=\s(.*)",line)
            if is_operation:
                monkey.operation = is_operation.groups(1)[0]

            is_test = re.match("^\s+Test:\sdivisible\sby\s(\d+)",line)
            if is_test:
                monkey.divisor = int(is_test.groups(1)[0])

            is_true_test = re.match("\s+If\strue:\sthrow\sto\smonkey\s(\d+)",line)
            if is_true_test:
                monkey.true_throw = int(is_true_test.groups(1)[0])

            is_false_test = re.match("\s+If\sfalse:\sthrow\sto\smonkey\s(\d+)",line)
            if is_false_test:
                monkey.false_throw = int(is_false_test.groups(1)[0])
        monkeys.append( monkey )

    # take a backup for use in part 2
    backup_monkeys = copy.deepcopy( monkeys )

    print("1.", play( monkeys, 20))

    # restore backup
    monkeys = copy.deepcopy( backup_monkeys )

    # set a monkey field to be the product of all unique divisors
    set_multiple_of_divisors( monkeys )

    print("2.", play( monkeys, 10000))
