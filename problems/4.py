def isPalindrome(n):
    rev = 0
    x = n
    while x > 0:
        rev = (10 * rev) + (x % 10)
        x /= 10
    return n == rev

def largestPalindromeProduct():
    max = 100001 #smallest palindrome with two 3 digit numbers
    for x in range(999, 99, -1):
        if max >= x * 999:
            break
        for y in range(999, x-1, -1):
            product = x * y
            if product > max and isPalindrome(product):
                max = product
    return max
print largestPalindromeProduct()
