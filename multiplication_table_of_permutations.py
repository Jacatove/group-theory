#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import permutations

from tabulate import tabulate


class permutation_function:
    def __init__(self, permutation):
        self.permutation = permutation

    def __repr__(self):
        return str(self.permutation)

    def __mul__(self, other):

        assert len(self.permutation) == len(other.permutation), 'permutations of different sizes.'

        result = []
        for i, element in enumerate(self.permutation):
            result.append(
                other.permutation[self.permutation[i]-1]
            )

        return tuple(result)

def generate_table():
    rows = []
    for row in functions:
        columns = [row]
        for col in functions:
            columns.append(col * row)
        rows.append(columns)

    return rows


if __name__=='__main__':

    while True:

        num_elements = int(input('Enter the number of the group of permutations S#: '))

        elements = tuple(range(1, num_elements+1))
        functions = [permutation_function(permutation) for permutation in permutations(elements)]

        print(
            tabulate(
                generate_table(),
                headers=functions,
                tablefmt='fancy_grid',
                stralign='center',
                numalign='center',
                floatfmt=".2f",
            )
        )

