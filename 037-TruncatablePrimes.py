#Problem 37: The number 3797 has an interesting property. Being prime itself, it is 
#possible to continuously remove digits from left to right, and remain prime at each 
#stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 
#3. Find the sum of the only eleven primes that are both truncatable from left to right 
#and right to left. NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

print("done")
def below(num):
    primes=[2]
    i=3
    while primes[-1]<num:
        isComposite = False
        k=0
        while primes[k]<=i**1/2:
            if(i%primes[k]==0):
                isComposite=True
                break
            k+=1
        if(not(isComposite)):
            primes.append(i)
        i+=2
    return primes

primes=below(1000000)
print("done!")
truncatable=[]
for p in primes:
    isTruncatable=True
    strp=str(p)
    for i in range(1, len(strp)):
        truncation=strp[i:]
        if int(truncation) not in primes:
            isTruncatable=False
        truncation=strp[:i]
        if int(truncation) not in primes:
            isTruncatable=False
    if isTruncatable:
        truncatable.append(p)

print(truncatable)
print(len(truncatable))

sum=0
for n in truncatable:
    sum=sum+n
print(sum)
