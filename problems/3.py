def largestPrimeFactor(n):
    factor = 2
    while factor < n:
        if n % factor == 0:
            n /= factor
            factor -= 1
        factor += 1
    return n

print largestPrimeFactor(600851475143)
