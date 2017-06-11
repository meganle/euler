def isPrime(n):
    if n % 2 == 0:
        return False
    p = 3
    while p < n**0.5+1:
        if n % p == 0:
            return False
        p += 2
    return True

def problem7(n):
    primeCount = 6
    start = 13
    while primeCount != n:
        start += 2
        if isPrime(start):
            primeCount += 1
    return start

print problem7(10001)
