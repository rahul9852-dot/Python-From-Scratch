'''In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation
Fn = Fn-1 + Fn-2
with seed values
F0 = 0 and F1 = 1.'''

def fib(n):
    a=0
    b=1
    if n<=0:
        return 0
    elif n==0:
        return 0
    elif n==1:
        return b
    else:
        for i in range(2,n):
            c=a+b
            a=b
            b=c
        return b
print(fib(9))


# Program to check either they are fibonacci or not

import math

def isperfect(x):
    s=int(math.sqrt(x))
    return s*s==x
def isfibonacci(n):
    
    # n is fibonacci if one of (5*n*n+4) or (5*n*n-4)
    # or both is perfectsquare

    return isperfect(5*n*n+4) or isperfect(5*n*n-4)
isfibonacci(8)
for i in range(1,11):
    if isfibonacci(i)==True:
        print(i," is a fibonacci number.")
    else:
        print(i," is not a fibonacci number.")

