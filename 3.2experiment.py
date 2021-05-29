"""
3.2) Implement a python script using
for loop that loops over a sequence
"""
#for variable in range(start,end+1)
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))  
for num in range(start, end + 1):
     # checking condition
        if num % 2 == 0:
            print(num, end = " ")          
#output
Enter the start of range: 2
Enter the end of range: 12
2 4 6 8 10 12
#for variable in string
str="SAI SREE"
for i in str:
    print(i)
#output
S
A
I
 
S
R
E
E
#for variable in list
l=[1,2,3,4,5]
for i in l:
    print(i)
#output
1
2
3
4
5
#for variablenin range(value)
for i in range(6):
    print(i)
#output
0
1
2
3
4
5
#for variable in range(start,end,incre/decre)
for i in range(1,6,2):
    print(i)
#output
1
3
5
    


    
