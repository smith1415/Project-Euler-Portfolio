#Problem 47: The first two consecutive numbers to have two distinct prime factors are: 
"""
14=2*7
15=3*5
"""
#The first three consecutive numbers to have three distinct prime factors are:
"""
644=2^2*7*23
645=3*5*43
646=2*17*19
""" 
#Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

print("starting")
def isComposite(num):
    k=0
    while primes[k]<=num**1/2:
        if(num%primes[k]==0):
            return True
        k+=1
    primes.append(num)
    return False

def numOfFactors(num, start, count):
    if num==1:
        return count
    for i in range(start, len(primes)):
        if num%primes[i]==0:
            while num%primes[i]==0:
                num=int(num/primes[i])
            return numOfFactors(num, i+1, count+1)
        

primes=[2]
i=3
notFound=True
prev=[0,0]
prev2=[0,0]
prev3=[0,0]
while notFound:
    if isComposite(i):
        num=numOfFactors(i, 0, 0)
        if num==4 and prev[1]==4 and prev2[1]==4 and prev3[1]==4:
            print(prev3[0], "has", prev3[1])
            print(prev2[0], "has", prev2[1])
            print(prev[0], "has", prev[1])
            print(i, "has", num)
            notFound=False
    else:
        num=1
    prev3[0]=prev2[0]
    prev3[1]=prev2[1]
    prev2[0]=prev[0]
    prev2[1]=prev[1]
    prev[0]=i
    prev[1]=num
    i+=1
