n = int(input())
arr = []
count = 0
while len(arr) < n:
    line = input().split() 
    for x in line:
        arr.append(int(x))
for i in range(len(arr) - 1):
    if (arr[i+1] > arr[i]):
        count += 1
print(count)