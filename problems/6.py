def problem6(n):
    sumOfSquares = 0
    sum = 0
    for x in range(1, n+1):
        sumOfSquares += x * x
        sum += x
    return (sum * sum) - sumOfSquares

print problem6(100)
