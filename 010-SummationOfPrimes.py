#Problem 10: The sum of the primes below 10 is 2+3+5+7=17. Find the sum of all the 
#primes below two million.

def isPrime(num):
    k=0
    while primes[k]<=num**1/2:
        if(num%primes[k]==0):
            return False
        k+=1
    return True
    
num=int(input("The sum of the primes below what number?"))
primes=[2]
sum=2
i=3
while i<num:
    if(isPrime(i)):
        sum+=i
        primes.append(i)
    i+=2

print(sum)
