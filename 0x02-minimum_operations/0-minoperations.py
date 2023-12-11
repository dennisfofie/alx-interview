#!/usr/bin/python3
"""returns the minimum number to copy and paste"""


def minOperations(n: int) -> int:
    """minimum number of occurence using prime factors"""
    results = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            results.append(divisor)
            n /= divisor
        else:
            divisor += 1
    return sum(results)
