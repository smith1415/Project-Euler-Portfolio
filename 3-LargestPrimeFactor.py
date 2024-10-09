#Problem 3:The prime factors of 13195 are 5, 7, 13, and 29. What is the largest prime factor of the number 600851475143?

"""First Attempt
def isPrime(num):
    for i in range(2, int(num**1/2)+1):
        if num%i==0:
            return False
    return True
def largestPrimeFactor(num):
    j=num
    while j>0:
        if num%j==0 and isPrime(j):
            return j
        j-=1
number=int(input("What number do you want?"))
print(str(largestPrimeFactor(number)))"""


"""Second Attempt
def largestPrimeFactor(num):
    primes=[2]
    for i in range(3, num+1):
        isComposite = False
        k=0
        while primes[k]<=i**1/2:
            if(i%primes[k]==0):
                isComposite=True
            k+=1
        if(not(isComposite)):
            primes.append(i)
    for j in range(0, len(primes)):
        if(num%primes[len(primes)-1-j]==0):
            return primes[len(primes)-1-j]

n=int(input("What number do you want?"))
print(largestPrimeFactor(n))
"""

"""Third attempt
def largestPrimeFactor(num):
    tinyPrimes=[2]
    for i in range(3, int(num**(1/2))+1):
        isComposite = False
        k=0
        while tinyPrimes[k]<=i**(1/2):
            if(i%tinyPrimes[k]==0):
                isComposite=True
            k+=1
        if(not(isComposite)):
            tinyPrimes.append(i)
    print(tinyPrimes)
    candidate=num
    while candidate > num**(1/2):
        if num%candidate==0:
            isComposite = False
            k=0
            while k<len(tinyPrimes) and tinyPrimes[k]<=candidate**(1/2):
                if(candidate%tinyPrimes[k]==0):
                    isComposite=True
                k+=1
            if(not(isComposite)):
                return candidate
        candidate-=1
    while candidate > 1:
        if num%candidate==0:
            if candidate in tinyPrimes:
                return candidate
        candidate-=1
n=int(input("What number do you want?"))
print(largestPrimeFactor(n))"""

"""Fourth attempt
def how(n):
    return (int(n**(1/2))+1)

def findLowestMultiples(num, start, end, array):
    nothing=True
    for i  in range(start, end):
        if num%i==0:
            array.append(i)
            return findLowestMultiples(int(num/i), i, how(int(num/i)), array)
    if(nothing):
        return [num, array]
            
def largestPrimeFactor(num):
    primes=[2]
    for i in range(3, num+1):
        isComposite = False
        k=0
        while primes[k]<=i**1/2:
            if(i%primes[k]==0):
                isComposite=True
            k+=1
        if(not(isComposite)):
            primes.append(i)
    for j in range(0, len(primes)):
        if(num%primes[len(primes)-1-j]==0):
            return primes[len(primes)-1-j]

    
n=int(input("What number do you want?"))
f=findLowestMultiples(n, 2, how(n), [])
print(f)
print(largestPrimeFactor(f[0]))
"""

#Fifth #5
def findLowestMultiples(num, start, end, array):
    for i  in range(start, end):
        if num%i==0:
            array.append(i)
            return findLowestMultiples(int(num/i), i, int(num/i)+1, array)
    return array

n=int(input("What number do you want?"))
f=findLowestMultiples(n, 2, n+1, [])
print(f)
print(f[-1])
