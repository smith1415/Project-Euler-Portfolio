#Problem 97: The first known prime found to exceed one million digits was discovered in 
#1999, and is a Mersenne prime of the form 2**6972593-1; it contains exactly 2098960 
#digits. Subsequently other Mersenne primes, of the form 2**p-1, have been found which 
#contain more digits. However, in 2004 there was found a massive non-Mersenne prime which 
#contains 2357207 digits: 28433*2**7830457+1. Find the last ten digits of this prime 
#number.

#7830457/8=978807 R1
power=2
for i in range(0, 978807):
    power*=256
    power=power%10000000000
a=power*28433+1
print(a%10000000000)
