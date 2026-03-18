n = int(input())
arr = []
count = 0
while len(arr) < n:
    line = input().split() 
    for x in line:
        arr.append(int(x))
for i in range(len(arr)):
    if (arr[i] % 2 == 0):
        count += 1
print(count)
