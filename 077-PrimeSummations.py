#Problem 77: It is possible to write ten as the sum of primes in exactly five different ways:
"""
7+3
5+5
5+3+2
3+3+2+2
2+2+2+2+2
"""
#What is the first value which can be written as the sum of primes in over five thousand 
#different ways?

#c.f. problems 76, 31, and 0
booleans=[False, False]
for i in range(2, 1000):
    booleans.append(True)

for i in range(2, 1000):
    if booleans[i]:
        for j in range(2*i, 1000, i):
            booleans[j]=False
primes=[]
for i in range(0, 1000):
    if booleans[i]:
        primes.append(i)

def primeWays(n, lowest, goal):
    if n>goal:
        return 0
    if n==goal:
        return 1
    else:
        i=0
        total=0
        while not(i==len(primes)) and primes[i]<=lowest:
            total=total+primeWays(primes[i], primes[i], goal-n)
            i+=1
    return total


#finds the list of ways
def primeListWays(nums, goal, finalList):
    if sum(nums)>goal:
        return 0
    if sum(nums)==goal:
        finalList.append(nums)
        return 1
    else:
        i=0
        total=0
        while not(i==len(primes)) and primes[i]<=nums[-1]:
            newnums=[]
            for n in nums:
                newnums.append(n)
            newnums.append(primes[i])
            total=total+primeListWays(newnums, goal, finalList)
            i+=1
        return total
def primeGroupings(num, listing):
    out=0
    for i in primes:
        out=out+primeListWays([i], num, listing)
    return out

i=1
#number of prime summations
nps=1

while nps<=5000:
    i+=1
    nps=primeWays(0, i, i)
    print(i, nps)
print("Answer:", i)
groups=[]
primeGroupings(i, groups)
for g in groups:
    print(g)
