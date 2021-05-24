"""
5.3) Implement a python script to count number of words
in a string and reverse each word in a string at the same location.
Example: Input :Honesty is the best policy Output :5 ytseno Hsiehttsebycilops= input("Enter the string: ")
"""
res = len(s.split())
print ("The number of words in string are : " +  str(res))
w = s.split(" ")
nw = [i[::-1] for i in w]
ns = " ".join(nw)
print(ns)

#output
Enter the string: Iam Sai Sree from CSE A
The number of words in string are : 6
maI iaS eerS morf ESC A
