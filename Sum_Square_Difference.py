# Problem statement link --> https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem
#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum_squares = (n * (n+1) * (2*n+1))//6
    sq_sum = ((n * (n+1))//2) ** 2
    print(abs(sum_squares - sq_sum))