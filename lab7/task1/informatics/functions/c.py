def xor(a,b):
    if (a == b):
        return 0
    return 1

line = input().split()
a = int(line[0])
b = int(line[1])
print(xor(a, b))