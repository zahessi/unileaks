def eratosphen(n):
    primes = [2]
    divisable = None
    for i in range(3, n):
        divisable = False
        for n in primes:
            if i % n == 0: 
                divisable = True
                break
        if not divisable: primes.append(i)
    return primes

print(eratosphen(100000))
