a = int(input())

if (a%2 == 1 or (a%2 == 0 and a >= 6 and a <= 20)):
    print("Weird")
else:
    print("Not Weird")