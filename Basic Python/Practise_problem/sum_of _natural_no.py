# python program for sum of squares of first n natural number.

# given a positive integer N. The task is to find 1^2+2^2+3^2....+N^2.

def sum_natural_number(n):
    return (n*(n+1)*(2*n+1))/6
print(sum_natural_number(4))

def sum_natural(n):
    sum=0
    for i in range(1,n+1):
        sum+=i*i
    return sum
print(sum_natural(4))