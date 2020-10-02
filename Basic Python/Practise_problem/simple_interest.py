# program through simple Interest 
'''Simple interest formula is given by:
Simple Interest = (P x T x R)/100
Where,
P is the principle amount
T is the time and
R is the rate'''
'''
Input : P = 10000
        R = 5
        T = 5
Output :2500
We need to find simple interest on 
Rs. 10,000 at the rate of 5% for 5 
units of time.

EXAMPLE2:
Input : P = 3000
        R = 7
        T = 1
Output :210'''

def calc_SI(P,R,T):
    SI=(P*R*T)/100
    return SI

principal=int(input())
rate=int(input())
time=int(input())
print(calc_SI(principal,rate,time))