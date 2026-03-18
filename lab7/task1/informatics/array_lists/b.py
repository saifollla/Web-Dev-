n = int(input())
arr = []
while (len(arr) < n):
    line = input().split() 
    for x in line:
        arr.append(int(x))

for i in range(len(arr)):
    if (arr[i] % 2 == 0):
        print(arr[i], end=' ')