# Python Program for array rotation 

# A function rotate(arr[],d,n) that rotates arr[] of size n by d elements.

# function to left rotatee arr[] of size n by d*/
def leftrotate(arr,d,n):
    for i in range(d):
        leftrotatebyone(arr,n)

# Function to left rotate arr[] of size n by 1*/

def leftrotatebyone(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp

def printarray(arr,size):
    for i in range(size):
        print("%d" % arr[i],end=" ")

arr=[1,2,3,4,5,6,7]
leftrotate(arr,2,7)
printarray(arr,7)
