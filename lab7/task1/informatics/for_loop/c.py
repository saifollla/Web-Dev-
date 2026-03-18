import math
a,b= int(input()), int(input())
start = math.ceil(a**0.5)
for i in range(start, int(b**0.5)+1):
    sq = i**2
    if sq <= b:
        print(sq) 