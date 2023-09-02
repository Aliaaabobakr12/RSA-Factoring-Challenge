#!/usr/bin/python3

import time
import math
import sys

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    
    x = 2
    y = 2
    d = 1
    
    f = lambda x: (x**2 + 1) % n
    
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = math.gcd(abs(x - y), n)
    
    return d

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def main():
    if len(sys.argv) != 2:
        print("Usage: python factorize.py <file>")
        return

    file_path = sys.argv[1]

    start_time = time.time()
    try:
        with open(file_path, 'r') as file:
            number = int(file.readline().strip())
        p = pollard_rho(number)
        while not is_prime(p):
            p = pollard_rho(p)
        q = number // p
        if p == number or q == number:
            print("{} is prime.".format(number))
        else:
            print("{}={}*{}".format(number, p, q))

        if time.time() - start_time > 5:
            print("Time limit exceeded")
            exit()
    
    except FileNotFoundError:
        print("File '{}' not found.".format(file_path))


if __name__ == '__main__':
    main()
