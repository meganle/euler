sum = 0
for value in range(1,1000):
    if value % 5 == 0:
        sum += value
    elif value % 3 == 0:
        sum += value

print sum
