s= input("Enter the string: ")
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
