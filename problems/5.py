def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x%y)

def lcm(n):
    num = 1
    for x in range(2, n+1):
        num = (num * x) / gcd(x, num)
    return num

print lcm(20)
