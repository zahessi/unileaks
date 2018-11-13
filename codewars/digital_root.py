# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n):
    if n < 10:
        return n
    else: 
        s = 0
        while n > 0:
            s += n % 10
            n = n // 10
        return digital_root(s) 

assert digital_root(16) == 7