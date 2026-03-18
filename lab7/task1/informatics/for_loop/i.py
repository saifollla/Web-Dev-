a = int(input())
count = 0

for i in range(1, int(a**0.5) + 1):
    if a % i == 0:
        if i * i == a:
            count += 1  
        else:
            count += 2  

print(count)