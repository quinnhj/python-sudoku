#!/usr/bin/env python

import sys
import copy

def reject(c):
    return False

def accept(c):
    if reject(c):
        return False
    for line in c:
        if any(0 in i for i in line):
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
    extensions = extensions(c)
    for e in extensions:
        res = backtrack(e)
        if res:
            return res 
    return False

if __name__ == "__main__":
    puzzle = []
    print "Doing nuthin"
    print "Filename: " + sys.argv[1]
    with open(sys.argv[1], 'r') as f:
        for line in f:
            puzzle.append(map(int, list(line)[:-1]))
    print puzzle



