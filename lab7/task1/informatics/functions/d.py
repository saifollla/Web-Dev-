def election(a,b,c):
    sum = a + b + c
    if sum >= 2:
        return 1
    else:
        return 0
    
line = input().split()
a = int(line[0])    
b = int(line[1])
c = int(line[2])
print(election(a, b, c))