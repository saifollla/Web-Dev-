a = int(input())
res = 1
for i in range(2, int(a**0.5)+1):
    if a % i == 0:
        res = i
        break
print(res)