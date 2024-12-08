#Problem 23: A perfect number is a number for which the sum of its proper divisors is 
#exactly equal to the number. For example, the sum of the proper divisors of 28 would be 
#1+2+4+7+14=28, which means that 28 is a perfect number. A number n is called deficient if 
#the sum of its proper divisors is less than n and it is called abundant if this sum 
#exceeds n. As 12 is the smallest abundant number, 1+2+3+4+6=16, the smallest number that 
#can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can 
#be shown that all integers greater than 28123 can be written as the sum of two abundant 
#numbers. However, this upper limit cannot be reduced any further by analysis even though 
#it is known that the greatest number that cannot be expressed as the sum of two abundant 
#numbers is less than this limit. Find the sum of all the positive integers which cannot 
#be written as the sum of two abundant numbers.

def factorize(num):
    array=[1]
    for i in range(2,int(num**(1/2)+1)):
        if(num%i==0):
            array.append(i)
            if(not(int(num/i)==i)):
                array.append(int(num/i))
    return array

abundants=[]
for i in range(2, 28124):
    factors=factorize(i)
    sum=0
    for n in factors:
        sum=sum+n
    if sum>i:
        abundants.append(i)
print("factorization done.")

#I did a whole separate thing for the multiples of abundant numbers oops
"""#remove multiples from list of abundants
for n in abundants:
    l = len(abundants)
    for i in range(1, len(abundants)+1):
        if (abundants[l-i]%n==0):
            if not(abundants[l-i]==n):
                abundants.remove(abundants[l-i])

#get a list of all of the integers 0-29123 inclusive
numbers=[]
for i in range(0, 28124):
    numbers.append(i)

#mark the numbers that are the multiples of an abundunt by making them floats
for a in abundants:
    index=a
    while index<28124:
        valueAtIndex=numbers[index]
        numbers.remove(valueAtIndex)
        numbers.insert(index, valueAtIndex/1)
        index=index+a

sum = 0
for n in numbers:
    if isinstance(n, int):
        sum=sum+n

print(sum)
"""

#make a list of all the positive integers up to 28123
numbers=[]
for i in range(1, 28124):
    numbers.append(i)

print("list made.")

#remove each sum of two abundants
for i in range (0, len(abundants)):
    for j in range (i, len(abundants)):
        sum=abundants[i]+abundants[j]
        if sum in numbers:
            numbers.remove(sum)
print("sums removed.")


#sum the ones left
sum = 0
for n in numbers:
    sum=sum+n
print("non-sums summed.")

print("answer:", sum)
