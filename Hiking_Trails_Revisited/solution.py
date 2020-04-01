#!/usr/bin/env python3
"""
File: solution.py
Authors: Ambroise Renaud, Johan Barthas, Yu Tianchi
Description: Homework1 solution
"""


def greedy(f, n, y, hn):
    """
    Implementation of greedy algorithm

    cf Homework for detail

    Parameters
    ----------
    f : array-like
        array of arrays representing the locations
    n : int
        number of trails
    y : array-like
        budget in trail order
    hn : float
        harmonic number

    Returns
    -------
    solution
        array of locations
    y
        array of budgets
    """
    c = set()
    solution = []
    while len(c) != n:
        _, a = argmax(compute_diff(c, f))
        solution.append(a + 1)

        price = 1 / (hn * diff(c, f[a][1:]))
        for x in f[a][1:]:
            if x not in c:
                y[x - 1] = price
        c = c.union(set(f[a][1:]))
    return solution, y


def compute_diff(c, f):
    """
    Compute the difference of set, set-wise


    Parameters
    ----------
    c : array-like
        array
    f : array-like
        array of arrays

    Returns
    -------
    diff
        array of the remaing sets length in location order
    """
    _diff = []
    for x in f:
        _diff.append(diff(c, x[1:]))
    return _diff


def argmax(_list):
    """
    Compute argmax of a list

    Previous maximum is not overwrited

    Parameters
    ----------
    _list : array-like
        list to find argmax

    Returns
    -------

    _max
        maximum value
    argmax
        maximum index
    """
    _max = _list[0]
    argmax = 0
    for i, x in enumerate(_list):
        if x > _max:
            _max = x
            argmax = i
    return _max, argmax


def diff(a, b):
    """
    Compute difference between two sets

    As stated in the homework pseudocode of Greedy : S \ C or A \ C

    Parameters
    ----------
    a : array-like
        first set
    b : array-like
        second set

    Returns
    -------
    len(b) - common
        length of the remaining set
    """
    common = 0
    for x in b:
        if x in a:
            common += 1
    return len(b) - common


def harmonic(n):
    """
    Compute the n-th Harmonic number

    Compute Hn where Hn = 1 + 1/2 + 1/3 + ... + 1/n

    Parameters
    ----------
    n : int
        n-th number

    Returns
    -------
    hn
        harmonic number
    """
    hn = 0
    for i in range(1, n):
        hn += 1 / i
    return hn


if __name__ == "__main__":
    # Input
    n, m = [int(x) for x in input().split()]
    trails = [[int(x) for x in input().split()] for i in range(m)]

    # Budget
    y = [0 for _ in range(n)]
    # Hn
    hn = harmonic(n)

    # Compute the solution
    solution, y = greedy(trails, n, y, hn)

    # Output the solution
    print(len(solution))
    for x in solution:
        print(x, end=" ")

    print()
    for x in y:
        print(round(x, 6), end=" ")
