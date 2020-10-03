# Python program to find largest element in an array

def largest_ele(array,n):
    islargest=array[0]
    for i in range(0,n):
        if arr[i]>islargest:
            islargest=arr[i]
    return islargest
    
arr=[10,2,4,5,12]
n=len(arr)
print(largest_ele(arr,n))