#!/usr/bin/env python

import sys
import copy

class Sudoku:
    
    def __init__(self, l):
        self.board = l

    def get(self, x, y):
        return self.board[y][x]

    def set(self, x, y, val):
        self.board[y][x] = val
    
    def isFilled(self):
        for line in self.board:
            if 0 in line:
                return False
        return True

def check_unique(l):
    trimmed = [i for i in l if i != 0]
    return len(trimmed) == len(set(trimmed))

def check_box(c, xs, ys):
    l = []
    for x in range(xs, xs+3):
        for y in range(ys, ys+3):
            l.append(c.get(x,y))
    return check_unique(l)

def check_row(c, y):
    l = []
    for x in range(9):
        l.append(c.get(x,y))
    return check_unique(l)

def check_col(c, x):
    l = []
    for y in range(9):
        l.append(c.get(x,y))
    return check_unique(l)

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
    return c.isFilled()

def extensions(c):
    extension_list = []
    for x in range(9):
        for y in range(9):
            val = c.get(x,y)
            if val == 0:
                for i in range(1,10):
                    new_c = copy.deepcopy(c)
                    new_c.set(x,y,i)
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
    sol = backtrack(Sudoku(puzzle))
    if sol:
        for line in sol.board:
            print " ".join(map(str, line))
    else:
        print "Couldn't find a solution"

