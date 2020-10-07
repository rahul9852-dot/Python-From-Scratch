# Python program tomswap elements at given positions

# Defining Function
def swap(alist,pos1,pos2):

    # Swaping element w.r.t given position
    alist[pos1],alist[pos2]=alist[pos2],alist[pos1]
    return alist

# Test code
alist=[23,65,19,90]
pos1,pos2=1,3
print("Before interchanging position element are :",alist)
print("After changing position of element:",swap(alist,pos1-1,pos2-1))

