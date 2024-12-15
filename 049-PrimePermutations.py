#Problem 49: The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another. There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence. What 12-digit number do you form by concatenating the three terms in this sequence?

def isPrime(num):
    k=0
    while primes[k]<=num**1/2:
        if(num%primes[k]==0):
            return False
        k+=1
    primes.append(num)
    return True

def arePermutations(a, b):
    stra=str(a)
    strb=str(b)
    digits=[]
    for digit in stra:
        digits.append(digit)
    for digit in strb:
        if digit in digits:
            digits.remove(digit)
        else:
            return False
    return True

primes=[2]
notFound=True
for i in range(3, 1000, 2):
    isPrime(i)

i=999
fourDigitPrimes=[]
while notFound:
    i+=2
    if isPrime(i):
        fourDigitPrimes.append(i)
        perm=[]
        for p in fourDigitPrimes:
            if arePermutations(i, p):
                perm.append(p)
        if len(perm)>2:
            d=[]
            for j in range(0, len(perm)):
                for k in range(j+1, len(perm)):
                    diff=perm[k]-perm[j]
                    d.append([j, k, diff])
            for j in range(0, len(d)):
                for k in range(j+1, len(d)):
                    if d[j][2]==d[k][2]:
                        if d[j][0]==d[k][1]:
                            triple=[perm[d[k][0]],perm[d[k][1]],perm[d[j][1]]]
                            print("FOUND!", triple, d[j][2], d[k][2])
                            notFound=False
                        elif d[j][1]==d[k][0]:
                            triple=[perm[d[j][0]],perm[d[j][1]],perm[d[k][1]]]
                            if not triple==[1487, 4817, 8147]:
                                print("Answer:", triple)
                                print("Difference:", d[k][2])
                                notFound=False
