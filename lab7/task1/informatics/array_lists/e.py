n = int(input())
arr = []
count = 0
while len(arr) < n:
    line = input().split() 
    for x in line:
        arr.append(int(x))
for i in range(len(arr) - 1):
    if (arr[i+1] >0 and  arr[i] > 0 or arr[i+1] < 0 and arr[i] < 0):
        print("YES")
        break
else:
    print("NO")