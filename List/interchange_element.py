# python program to swap first and last element.

# Defining Function

def swap(alist):
    # Swap
    alist[0],alist[-1]=alist[-1],alist[0]
    return alist

#program to test
alist=[12,35,9,56,24]
print("Before swaping element are in form:",alist)
print("After swaping of first and last element:")
print(swap(alist))
