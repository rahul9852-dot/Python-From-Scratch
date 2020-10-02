'''Given two positive integers start and end. The task is to write a Python program to print all Prime numbers in an Interval.
Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The first few prime numbers are {2, 3, 5, 7, 11, ….}.
The idea to solve this problem is to iterate the val from start to end using a 
for loop and for every number, if it is greater 
than 1, check if it divides n. If we find any other number which divides, print that value.'''

start=11
end=25
for i in range(start,end):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)


#Analysis of Different Methods to find Prime Number in Python

# Method 1:
'''Let us now go with the very first function to check whether a number, say n, is prime or not. In this method, we will test all divisors from 2 to n-1. We will skip 1 and n. If n is divisible by any of the divisor, the function will return False, else True.
Following are the steps used in this method:

If the integer is less than equal to 1, it returns False.
If the given number is divisible by any of the numbers from 2 to n, the function will return False
Else it will return True'''

import time
def prime_number(n):
    if n<=1:
        return False

    for i in range(2,n):
        if n%i==0:
            return False
    return True
t0=time.time()
c=0 # for counting

for n in range(1,100000):
    x=prime_number(n)
    c+=x
print("Total prime number in range :",c)

t1=time.time()
print("Time required :",t1-t0)

# Method 2:
'''We can optimise the algorithm to check whether number, say n, is a prime or not. In this method we will test all divisors from 2 to n/2.'''

def is_prime(num):
    for i in range(2, int(num/2)):
        if num % i == 0:
            return False
    return True


number = 110
print(is_prime(number))
