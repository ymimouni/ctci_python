"""
The Sieve of Eratosthenes.
"""

from typing import List
from math import sqrt


def sieve_of_eratosthenes(m: int) -> List[bool]:
    # Set all flags to true other than 0 and 1
    flags = [True] * (m + 1)
    flags[0] = flags[1] = False

    prime = 2
    while prime <= sqrt(m):
        # Cross of remaining multiples of prime
        cross_off(flags, prime)

        # Find next value which is true
        prime = get_next_prime(flags, prime)

    return flags


def cross_off(flags, prime):
    # Cross off remaining multiples of prime. We can start with prime * prime
    for i in range(prime * prime, len(flags), prime):
        flags[i] = False


def get_next_prime(flags, prime):
    n = prime + 1
    while n < len(flags) and not flags[n]:
        n += 1

    return n


if __name__ == "__main__":
    print(sieve_of_eratosthenes(100))
