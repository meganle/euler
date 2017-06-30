def problem6(n):
    nsum = (n*(n+1))/2
    nsum_sq = ((2*n+1)*(n+1)*n)/6
    return nsum**2 - nsum_sq

print problem6(100)
