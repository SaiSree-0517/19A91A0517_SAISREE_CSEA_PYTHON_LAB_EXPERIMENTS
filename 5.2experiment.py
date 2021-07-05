"""
5.2) Write a program to use split and join methods
in the string and trace a birthday with a dictionary data structure.
"""
d={"Ram":"15/07/1989", "Krishna":"09/12/1988","Venkat":"11/02/2016"}
dat=input("enter date")
x=dat.split('-')
print(x)
dob='/'.join(x)
print(dob)
if dob in d.values():
    print('Date of Birth is found in the birthday dictionary')
else:
    print('Date of Birth is not found')
"""
output1:
enter date15/07/1989
['15/07/1989']
15/07/1989
Date of Birth is found in the birthday dictionary
output2:
enter date16/7/1989
['16/7/1989']
16/7/1989
Date of Birth is not found
"""
