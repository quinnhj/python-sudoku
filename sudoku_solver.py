#!/usr/bin/env python

import sys
import copy

def check_box(c, xs, ys):
    seen = set()
    for x in range(xs, xs+3):
        for y in range(ys, ys+3):
            if c[y][x] in seen:
                return False
            if not c[y][x] == 0:
                seen.add(c[y][x])
    return True

def check_row(c, y):
    seen = set()
    for x in range(9):
        if c[y][x] in seen:
            return False
        if not c[y][x] == 0:
            seen.add(c[y][x])
    return True

def check_col(c, x):
    seen = set()
    for y in range(9):
        if c[y][x] in seen:
            return False
        if not c[y][x] == 0:
            seen.add(c[y][x])
    return True

def reject(c):
    for i in range(9):
        if (not check_col(c, i)) or (not check_row(c, i)):
            return True
    for a in [0,3,6]:
        for b in [0,3,6]:
            if not check_box(c, a, b):
                return True
    return False

def accept(c):
    if reject(c):
        return False
    for line in c:
        if 0 in line:
            return False
    return True

def extensions(c):
    extension_list = []
    for line_num, line in enumerate(c):
        for idx, val in enumerate(line):
            if val == 0:
                for i in range(1, 10):
                    new_c = copy.deepcopy(c)
                    new_c[line_num][idx] = i
                    extension_list.append(new_c)
                return extension_list 
    return extension_list

def backtrack(c):
    if reject(c):
        return False
    if accept(c):
        return c
    extension_list = extensions(c)
    for e in extension_list:
        res = backtrack(e)
        if res:
            return res 
    return False

if __name__ == "__main__":
    puzzle = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            puzzle.append(map(int, list(line)[:-1]))
    sol = backtrack(puzzle)
    if sol:
        for line in sol:
            print " ".join(map(str, line))
    else:
        print "Couldn't find a solution"

