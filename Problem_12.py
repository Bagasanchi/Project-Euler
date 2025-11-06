import math

def sieve_primes(limit):
    """Return list of primes up to `limit` (inclusive) using Sieve of Eratosthenes."""
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            step = p
            start = p*p
            sieve[start: limit+1: step] = b"\x00" * (((limit - start) // step) + 1)
    return [i for i, isprime in enumerate(sieve) if isprime]

PRIMES = sieve_primes(100000)  # plenty for factorizing numbers up to tens/hundreds of millions

def prime_factorization(n):
    """Return prime factorization as dict {prime: exponent}."""
    factors = {}
    temp = n
    for p in PRIMES:
        if p * p > temp:
            break
        if temp % p == 0:
            exp = 0
            while temp % p == 0:
                temp //= p
                exp += 1
            factors[p] = exp
        if temp == 1:
            break
    if temp != 1:  # remaining prime
        factors[temp] = factors.get(temp, 0) + 1
    return factors

def num_divisors_from_factors(factors):
    """Given factor dict {p: e}, return number of divisors = product(e+1)."""
    res = 1
    for e in factors.values():
        res *= (e + 1)
    return res

def combined_divisor_count_for_triangle(n):
    """
    Compute number of divisors of T_n = n*(n+1)/2 efficiently by factorizing
    n and n+1 separately and adjusting for the 2 in the denominator.
    """
    a, b = n, n + 1
    # divide one of them by 2
    if a % 2 == 0:
        a //= 2
    else:
        b //= 2
    fa = prime_factorization(a)
    fb = prime_factorization(b)
    # since a and b now coprime, divisor count = d(a) * d(b)
    return num_divisors_from_factors(fa) * num_divisors_from_factors(fb)

def first_triangle_with_divisors(limit=500):
    n = 1
    while True:
        d = combined_divisor_count_for_triangle(n)
        if d > limit:
            triangle = n * (n + 1) // 2
            return triangle, n, d
        n += 1

if __name__ == "__main__":
    ans, index, divisors = first_triangle_with_divisors(500)
    print(f"First triangle number with over 500 divisors is {ans}")
    print(f"That's T_{index} = {index} * ({index}+1) / 2 with {divisors} divisors.")