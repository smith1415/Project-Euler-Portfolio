#Problem 7:By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. What is the 10001st prime number?

def primes(num):
    primes=[2]
    i=3
    while len(primes)<num:
        isPrime=True
        k=0
        while primes[k]<=i**1/2:
            if(i%primes[k]==0):
                isPrime=False
            k+=1
        if(isPrime):
            primes.append(i)
        i+=2
    return primes

n=int(input("What number do you want?"))
print(primes(n)[n-1])
