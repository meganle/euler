def problem9():
    for a in range(1, 1000):
        for b in range(a+1, 999):
            c = a**2 + b**2
            c = c**0.5
            if a + b + c == 1000:
                return a * b * c

print problem9()
