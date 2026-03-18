n = int(input())
arr = []
while len(arr) < n:
    line = input().split() 
    for x in line:
        arr.append(int(x))
for i in range(0, len(arr), 2):
    print(arr[i], end=' ')