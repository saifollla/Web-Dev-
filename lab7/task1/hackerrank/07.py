def sorting(char):
    if char.islower():
        priority = 0
    elif char.isupper():
        priority = 1
    elif char.isdigit():
        if int(char) % 2 != 0: 
            priority = 2
        else: 
            priority = 3
    else:
        priority= 4
    
    return (priority, char)
    

text = input()
sorted_chars = sorted(text, key=sorting)
result = "".join(sorted_chars)
print(result)