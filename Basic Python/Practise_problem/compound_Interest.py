'''Formula to calculate compound interest annually is given by:

A = P(1 + R/100) t
Compound Interest = A – P
Where,
A is amount
P is principle amount
R is the rate and
T is the time span'''

'''
Input : Principle (amount): 1200
        Time: 2
        Rate: 5.4
Output : Compound Interest = 1333.099243'''

def calc_CI(P,R,T):
    Amount=P*(pow((1+R/100),T))
    CI=Amount-P
    print("Compound Interest is",CI)
calc_CI(100000,3,36)