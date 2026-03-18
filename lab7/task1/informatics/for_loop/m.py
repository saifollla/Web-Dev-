a = int( input())
count = 0
for i in range(1, a + 1):
    b = int(input())
    if b == 0:
        count += 1
print(count)