#!/usr/bin/env python3
"""
File: solution.py
Authors: Ambroise Renaud, Johan Barthas, Yu Tianchi
Description: Homework1 solution
"""

def greedy(f, n, y, hn):
    c = set()
    solution = []
    while len(c) != n :
        _, a = argmax(compute_diff(c, f))
        solution.append(a+1)
        
        price = 1 / (hn * diff(c, f[a][1:]))
        for x in f[a][1:]:
            if x not in c:
                y[x-1] = price
        c = c.union(set(f[a][1:]))
    return solution, y

def compute_diff(c, f):
    _diff=[]
    for x in f:
        _diff.append(diff(c, x[1:]))
    return _diff

def argmax(_list):
    _max = _list[0]
    argmax = 0
    for i,x in enumerate(_list):
        if x> _max:
            _max = x
            argmax = i
    return _max, argmax

def diff(a, b):
    common = 0
    for x in b:
        if x in a:
            common +=1
    return len(b) - common

def harmonic(n):
    # """Compute H(n) = 1 + 1/2 + ... + 1/n."""
    # if n==1:
    #     return 1
    # elif n > 1:
    #     return harmonic(n-1) + 1/n
    # else:
    #     raise ValueError("Harmonic is undefined for this value: ", n)
    hn = 0
    for i in range(1, n):
        hn += 1/i
    return hn

# Input
n, m = [int(x) for x in input().split()]
trails = [[int(x) for x in input().split()] for i in range(m)]

# Budget
y = [0 for _ in range(n)]
# Hn
hn = harmonic(n)

solution, y = greedy(trails, n, y, hn)
print(len(solution))
for x in solution:
    print(x, end=' ')

print()
for x in y:
    print(round(x,6), end=' ')
