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