def is_palindrome(s):
    s = str(s)
    return s == s[::-1]

largest = 0
a = b = 0

for i in range(100, 1000):
    for j in range(100,1000):
        product = i * j
        if is_palindrome(product) and product > largest:
            largest = product
            a, b = i, j

print(f"Largest palindrome is {largest}, which is the product of {a} and {b}.")