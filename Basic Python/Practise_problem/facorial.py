
# Factorial of given number
# single line of code
# Recursive approach
def fact(n):
    return 1 if (n==1 or n==0) else n*fact(n-1)
print(fact(5))

# Iterative approach

def factorial(n):
    if n<0:
        return 0
    elif n==1 or n==0:
        return 1
    else:
        fact=1
        while n>1:
            fact*=n
            n-=1
        return fact
print(factorial(5))
    