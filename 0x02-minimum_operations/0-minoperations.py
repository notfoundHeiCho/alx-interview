#!/usr/bin/python3

"""Module containing function minoperations"""


def minOperations(n):
    if n == 1:
        return 0
    # Start with one 'H' character in the file
    operations = [0, 0]

    for i in range(2, n + 1):
        operations.append(float('inf'))

        for j in range(1, i // 2 + 1):
            if i % j == 0:
                operations[i] = min(operations[i], operations[j] + i // j)

    return operations[n]


# Test the function
n = 9
print(minOperations(n))
