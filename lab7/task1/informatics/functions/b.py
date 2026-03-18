def power(a, n):
    result = 1.0
    for i in range(n):
        result *= a
    return result

line = input().split()
a = float(line[0])
n = int(line[1])
print(power(a, n))