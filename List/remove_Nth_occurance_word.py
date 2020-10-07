'''# python program to remove Nth 
# occurance of the given word

# Function to remove Ith word
def removeIthword(lst,word,N):
    newlist=[]
    count=0

     # iterate the elements
    for i in lst:
        if (i==word):
            count+=1
            if count!=N:
                newlist.append(i)
            else:
                newlist.append(i)

    lst=newlist

    if count==0:
        print("Item not found")
    else:
        print("Update list: ",lst)

    return newlist

# program to test

list=["gekks","for","geeks"]
word="geeks"
N=2
removeIthword(list,word,N)'''

""" Identify co-prime pairs for all integers up (and not including limit 
 
identify all unique pairs - use integers m & n. 
 
Identify all unique prime factors for m & n 
 
Compare those sets of factors - if there is any overlapping factors then these values cannot be co-prime. 
""" 
'''prime_set = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97} 
 
limit = 100 
pairs = set() 
 
def factors( value ): 
    """identify unique prime factors for value""" 
    uniques = set() 
    for prime in prime_set: 
        if prime > value: 
            break 
        if value % prime == 0: 
            uniques.add(prime) 
    return uniques 
 
# Loop around all m from 2 to 100 inclusive 
for m in range(2, limit+1): 
	# Loop around all n from m to 100 - no point in n < 2 
    for n in range( n+1, limit+1): 
		# Identify unique factors of m & n 
        m_factors, n_factors = factors(m), factors(n) 
		# Identify any intersection between two sets. 
        if n_factors & m_factors == set(): 
			# No factors in common, so the pair is co-prime. 
            pairs.add((n,m)) 
print(len(pairs)) 
print(sorted(pairs)) '''



'''

# Python3 program to find number  
# of unordered coprime pairs of 
# integers from 1 to N 
N = 100
  
# to store euler's totient function 
phi = [0] * N 
  
# to store required answer 
S = [0] * N 
  
# Computes and prints totient of all  
# numbers smaller than or equal to N. 
def computeTotient(): 
  
    # Initialise the phi[] with 1 
    for i in range(1, N): 
        phi[i] = i 
  
    # Compute other Phi values 
    for p in range(2, N) : 
  
        # If phi[p] is not computed already, 
        # then number p is prime 
        if (phi[p] == p) : 
  
            # Phi of a prime number p  
            # is always equal to p-1. 
            phi[p] = p - 1
  
            # Update phi values of all 
            # multiples of p 
            for i in range(2 * p, N, p) : 
  
                # Add contribution of p to its 
                # multiple i by multiplying with 
                # (1 - 1/p) 
                phi[i] = (phi[i] // p) * (p - 1) 
  
# function to compute number  
# coprime pairs 
def CoPrimes(): 
      
    # function call to compute 
    # euler totient function 
    computeTotient() 
  
    # prefix sum of all euler  
    # totient function values 
    for i in range(1, N): 
        S[i] = S[i - 1] + phi[i] 
  
# Driver code 
if __name__ == "__main__": 
      
    # function call 
    CoPrimes() 
  
    q = [ 3, 4 ] 
    n = len(q) 
  
    for i in range(n): 
        print("Number of unordered coprime\n" + 
              "pairs of integers from 1 to ",  
               q[i], " are " , S[q[i]]) 
'''

# Python3 program to find maximum product by breaking  
# the Integer  
    
# method return x^a in log(a) time  
def power(x, a):  
   
    res = 1;  
    while (a): 
        if (a & 1):  
            res = res * x;  
        x = x * x;  
        a >>= 1; 
          
    return res; 
def breakInteger(N): 
    #  base case 2 = 1 + 1  
    if (N == 2):  
        return 1;  
    
    #  base case 3 = 2 + 1  
    if (N == 3):  
        return 2;  
    
    maxProduct=0;  
    
    #  breaking based on mod with 3  
    if(N % 3==0):  
        # If divides evenly, then break into all 3  
        maxProduct = power(3, int(N/3));  
        return maxProduct;  
    elif(N%3==1): 
        # If division gives mod as 1, then break as  
        # 4 + power of 3 for remaining part  
        maxProduct = 2 * 2 * power(3, int(N/3) - 1);  
        return maxProduct; 
    elif(N%3==2): 
        # If division gives mod as 2, then break as  
        # 2 + power of 3 for remaining part 
        maxProduct = 2 * power(3, int(N/3)); 
        return maxProduct; 
       
    
#  Driver code to test above methods  
  
   
maxProduct = breakInteger(7);  
print(maxProduct);