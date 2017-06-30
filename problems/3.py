def largestPrimeFactor(n):
    if n % 2 == 0:
    	last = 2
    	n /= 2
    	while n % 2 == 0:
    		n /= 2
    else:
    	last = 1
    factor = 3

    maxFactor = n**0.5
    while n > 1 and factor <= maxFactor:
    	if n % factor == 0:
    		n /= factor
    		last = factor
    		while n % factor == 0:
    			n /= factor
    		maxFactor = n**0.5
    	factor += 2
    if n == 1:
    	return last
    else:
    	return n
print largestPrimeFactor(600851475143)
