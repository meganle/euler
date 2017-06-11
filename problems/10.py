def isPrime(n):
    if n % 2 == 0 and n != 2:
        return False
    p = 3
    while p < n**0.5+1:
        if n % p == 0:
            return False
        p += 2
    return True

def problem10(x):
    sum = 2
    for value in range(3, x, 2):
        if isPrime(value):
            sum += value
    return sum

print problem10(2000000)
