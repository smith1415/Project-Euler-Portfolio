#Problem 35: The number, 197, is called a circular prime because all rotations of the 
#digits: 197, 971, and 719, are themselves prime. There are thirteen such primes below 
#100: 2,3,5,7,11,13,17,31,37,71,73,79 and 97. How many circular primes are there below one 
#million?

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
circular=[]
for p in primes:
    isCircular=True
    strp=str(p)
    for i in range(1, len(strp)):
        rotation=strp[i:]
        rotation=rotation+strp[:i]
        rotation=int(rotation)
        if rotation not in primes:
            isCircular=False
    if isCircular:
        circular.append(p)

print(circular)
print(len(circular))
