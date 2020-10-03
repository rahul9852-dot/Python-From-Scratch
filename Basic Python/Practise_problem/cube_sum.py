# python program to print the cube sum of first n natural numbers

def cubic_sum(n):
    return (n*(n+1)/2)**2
print(cubic_sum(5))

# Another approach
def cube_sum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i**3
    return sum
print(cube_sum(5))

