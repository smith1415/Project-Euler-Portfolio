#Problem 46: It was proposed by Christian Goldbach that every odd composite number can be 
#written as the sum of a prime and twice a square. 
"""
9=7+2(1)^2
15=7+2(2)^2
21=3+2(3)^2
25=7+2(3)^2
27=19+2(2)^2
33=31+2(1)^2
"""
#It turns out that the conjecture was false. What is the smallest odd composite that 
#cannot be written as the sum of a prime and twice a square?

def isComposite(num):
    k=0
    while primes[k]<=num**1/2:
        if(num%primes[k]==0):
            return True
        k+=1
    primes.append(num)
    return False

def hasSquare(num):
    for p in primes:
        squareroot=((num-p)/2)**(1/2)
        if squareroot==int(squareroot):
            print(num, "=", p, "+ 2 *", int(squareroot*squareroot))
            return True
    return False

primes=[2]
i=3
notFound=True
while notFound:
    if isComposite(i):
        if not(hasSquare(i)):
            print("Found:", i)
            notFound=False
    i+=2
