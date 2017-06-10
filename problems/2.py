first = 1
second = 2
term = first + second
sum = 2

while(term < 4000000):
    if term % 2 == 0:
        sum += term
    first = second
    second = term
    term = first + second

print sum
