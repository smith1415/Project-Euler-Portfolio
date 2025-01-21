#Problem 69: Euler's totient function, phi(n) [sometimes called the phi function], is 
#defined as the number of positive integers not exceeding n which are relatively prime to 
#n. For example, as 1, 2, 4, 5, 7, and 8, are all less than or equal to nine and 
#relatively prime to nine, phi(9)=6.
"""
n Relatively Prime	phi(n) n/phi(n)
2	1	              1      2
3	1,2	              2	     1.5
4	1,3	              2	     2
5	1,2,3,4	          4	     1.25
6	1,5	              2	     3
7	1,2,3,4,5,6	      6	     1.1666...
8	1,3,5,7	          4	     2
9	1,2,4,5,7,8	      6	     1.5
10	1,3,7,9	          4	     2.5
"""
#It can be seen that n=6 produces a maximum n/phi(n) for n<=10. Find the value of 
#n<=1000000 for which n/phi(n) is a maximum.

#version 1 (doesn't work):
""" 
def areRelPrime(num1, num2):
    if num1==1:
        return True
    remainder=num2%num1
    if remainder==0:
        return False
    while remainder>1:
        remainder=num1%remainder
        if remainder==0:
            return False
    return True
def totient(num):
    relPrimes=[]
    for i in range(1, num):
        if areRelPrime(i, num):
            relPrimes.append(i)
    print(relPrimes)
    return len(relPrimes)"""
#version 2:
def totient(num):
    list=[]
    for i in range(0, num):
        list.append(i)
    for i in range(2, num):
        item=list[i]
        if not item==num+1:
            if num%item==0:
                multiple=item
                while multiple<num:
                    list[multiple]=num+1
                    multiple=multiple+item
    while num+1 in list:
        list.remove(num+1)
    return len(list)-1

def step(num, ratio):
    if 2*num>1000001:
        return [num, ratio]
    for i in range(2*num, 1000001, num):
        t=totient(i)
        r=i/t
        if r>ratio:
            print(i, t, r)
            return [i, r]

#to be more efficient, I assume the next max is a multiple of the current max
#I'm not confident that this assumption is always true, but it worked out
coolestNum=1
maxRatio=1
notFound=True
while notFound:
    next=step(coolestNum, maxRatio)
    if coolestNum==next[0]:
        notFound=False
    else:
        coolestNum=next[0]
        maxRatio=next[1]
print("ANSWER:", coolestNum)
