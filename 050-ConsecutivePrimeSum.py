#Problem 50: The prime 41, can be written as the sum of six consecutive primes: 41=2+3+5+7+11+13. This is the longest sum of consecutive primes that adds to a prime below one-hundred. The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953. Which prime, below one-million, can be written as the sum of the most consecutive primes?

#This one took me forever
#it was so difficult for me to quickly find all the primes under a million
#I let it run long enough to find it once
#and tried to copy the list into the code directly
#but it was too long. it caused a memory error!
#I tried to separate into shorter lists, but still didn't work for me

#Thanks to Gabe Kane for talking about this problem with me!
#I did not understand what a prime sieve was at all.
#However, I had thought about something similar back in Sept (it is now Dec).
#I was solving problem 23 and I got confused.
#I tried to find the non-Abundant multiples not non-Abundant sums
#by traversing the list in jumps of abundant numbers
#and labeling each number it lands on to show that it is a multiple
#by making them floats instead of integers.
#It never occured to me to find primes with the same strategy
#omg it is so much faster!

booleans=[False, False]
for i in range(2, 1000001):
    booleans.append(True)

for i in range(2, 1000001):
    if booleans[i]:
        for j in range(2*i, 1000001, i):
            booleans[j]=False
primes=[]
for i in range(0, 1000000):
    if booleans[i]:
        primes.append(i)

list=[]
i=0
while sum(list)+primes[i]<primes[-1]:
    list.append(primes[i])
    i+=1
maxLen=len(list)

notFound=True
while notFound:
    list=[]
    for i in range(0, maxLen):
        list.append(primes[i])
    index=maxLen
    while sum(list)<1000000:
        if sum(list) in primes:
            print(sum(list), list)
            notFound=False
        list.pop(0)
        list.append(primes[index])
        index+=1
    maxLen-=1
    
