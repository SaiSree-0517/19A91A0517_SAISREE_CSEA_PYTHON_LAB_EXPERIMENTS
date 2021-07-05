#7.2) Find mean, median, mode for the given set of numbers in a list.
def mean(numlist):
    no_of_eles=len(numlist)
    summ=sum(numlist)
    avg=summ/no_of_eles
    print("Mean for given set of numbers is : ",avg)

def median(numlist):
    numlist.sort()
    if(len(numlist)%2!=0):
        i=len(numlist)//2
        print("Median for given set of numbers is : ",numlist[i])
    else:
        i=len(numlist)//2
        print("Median for given set of numbers is : ",(numlist[i-1]+numlist[i])/2)

def mode(numlist):
    count={}
    for j in numlist:
        if j in count:
            count[j]+=1
        else:
            count[j]=1
        countlist=count.values()
        maxcount=max(countlist)
        modelist=[]
        for j in count:
            if count[j]==maxcount:
                modelist.append(j)
   
    return modelist

numlist=[]
n=int(input("Enter number of elements to be insert:"))
for i in range(n):
    ele=int(input("Enter element:"))
    numlist.append(ele)
mean(numlist)
median(numlist)
md=mode(numlist)
print("mode of the given list is",md)
"""
Enter number of elements to be insert:10
Enter element:1
Enter element:2
Enter element:2
Enter element:2
Enter element:5
Enter element:6
Enter element:7
Enter element:7
Enter element:7
Enter element:7
Mean for given set of numbers is :  4.6
Median for given set of numbers is :  5.5
mode of the given list is [7]
"""
