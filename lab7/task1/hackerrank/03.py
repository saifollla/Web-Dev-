from itertools import groupby

def compress_the_string(s):
  
  for key, group in groupby(s):
    count = len(list(group))
    digit = int(key)
    print(f"({count}, {digit})", end=" ")

s = input()
compress_the_string(s)
print() 