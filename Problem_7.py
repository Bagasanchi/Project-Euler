import math

def is_prime(n):
    if n == 1:
        return 2
    if n < 6:
        upper = 15
    else:
        upper = int(n*(math.log(n) + math.log(math.log(n)))) + 3
    
    sieve = bytearray(b"\x01") * (upper + 1)
    sieve[0:2] = b"\x00\x00"
    p = 2
    while p * p <= upper:
        if sieve[p]:
            step = p
            start = p * p
            sieve[start: upper+1: step] = b"\x00" * (((upper - start) // step) + 1)
        p += 1

    count = 0
    for i, is_prime in enumerate(sieve):
        if is_prime:
            count += 1
            if count == n:
                return i

print(is_prime(10001))