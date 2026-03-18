def min_of_two(x, y):
    if x < y:
        return x
    return y

def min4(a, b, c, d):
    res1 = min_of_two(a, b)
    res2 = min_of_two(c, d)
    return min_of_two(res1, res2)
    
line = input().split()
a = int(line[0])
b = int(line[1])
c = int(line[2])
d = int(line[3])
print(min4(a, b, c, d))