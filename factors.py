#!/usr/bin/python3

import sys
import math
import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollard_rho(n):
    if n <= 1:
        return [(n, 1)]

    factors = []
    while n % 2 == 0:
        factors.append((2, n // 2))
        n //= 2

    if n == 1:
        return factors

    def rho(x, c):
        return (x * x + c) % n

    x, y, d = 2, 2, 1
    c = random.randint(1, n - 1)
    while d == 1:
        x = rho(x, c)
        y = rho(rho(y, c), c)
        d = gcd(abs(x - y), n)

    if d != n:
        factors.extend(pollard_rho(d))
        factors.extend(pollard_rho(n // d))
    else:
        factors.append((n, 1))

    return factors

if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)

input_file = sys.argv[1]

try:
    with open(input_file, 'r') as file:
        for line in file:
            n = int(line.strip())
            factors = pollard_rho(n)
            for p, q in factors:
                print("{}={}*{}".format(n, p, q))

except FileNotFoundError:
    print("File '{}' not found.".format(input_file))
    sys.exit(1)
except ValueError:
    print("Invalid input in the file. Please ensure all lines contain valid natural numbers greater than 1.")
    sys.exit(1)
