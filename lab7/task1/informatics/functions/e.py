import math

def is_prime(n):
    if n < 2:
        return "composite"
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return "composite"
            
    return "prime"


line = input().split()
n = int(line[0])
print(is_prime(n))