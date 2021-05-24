"""
5.1) Implement a python script to count frequency of characters in a given string.
"""
s=input("enter the string")
result = {}
for letter in s:
    if letter not in result:
          result[letter.lower()] = 1
    else:
          result[letter.lower()] += 1
print("count frequency of characters in given string:",result)
#output
enter the string hello world
count frequency of characters in given string: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
