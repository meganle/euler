limit = 4000000
sum = 10
a = 2
b = 8
c = 4 * b + a #only even fibonacci numbers

while c < limit:
    sum += c
    a = b
    b = c
    c = 4 * b + a

print sum
