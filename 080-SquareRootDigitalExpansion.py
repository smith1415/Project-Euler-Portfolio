#have not solved (yet)
#Problem 80: It is well known that if the square root of a natural number is not an integer, 
#then it is irrational. The decimal expansion of such square roots is infinite without any 
#repeating pattern at all. The square root of two is 1.41421356237309504880..., and the digital 
#sum of the first one hundred decimal digits is 475. For the first one hundred natural numbers, 
#find the total of the digital sums of the first one hundred decimal digits for all the 
#irrational square roots.

nonsquares=[]
for i in range(1, 101):
    nonsquares.append(i)
for i in range(1, 11):
    nonsquares.remove(int(i**2))
sum=0
for n in nonsquares:
    sqrt=n**(1/2)
    for i in range(1, 101):
        multiplied=sqrt*(10**i)
        sum=sum+(int(multiplied)%10)
    print(n, sum)
  
#the digits are wrong :(
sum=0
sqrt=2**(1/2)
print(sqrt)
for i in range(1, 101):
    multiplied=sqrt*(10**i)
    digit=int(multiplied)%10
    sum=sum+digit
    print(i, digit, sum)

