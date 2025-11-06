import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

num = 1
for i in range(1, 21):
    num = lcm(num, i)

print("1–20 бүх тоонд хуваагддаг хамгийн бага тоо =", num)