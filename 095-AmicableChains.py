#Problem 95: The proper divisors of a number are all the divisors excluding the number 
#itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of 
#these divisors is equal to 28, we call it a perfect number. Interestingly the sum of the 
#proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a 
#chain of two numbers. For this reason, 220 and 284 are called an amicable pair. Perhaps 
#less well known are longer chains. For example, starting with 12496, we form a chain of 
#five numbers: 12496->14288->15472->14536->14264(->12496->...). Since this chain returns 
#to its starting point, it is called an amicable chain. Find the smallest member of the 
#longest amicable chain with no element exceeding one million.

#cf Euler problem 21
def d(num):
    if num==0 or num==1:
        return 0
    if num==2 or num==3:
        return 1
    else:
        sum=1
        for i in range(2,int(num**(1/2)+1)):
            if(num%i==0):
                sum=sum+i
                if(not(int(num/i)==i)):
                    sum=sum+int(num/i)
    return sum

def loop(num):
    next=d(num)
    stage=1
    blocked=[0, next]
    if next>1000000:
        return -1
    while not next==num:
        next=d(next)
        if next>1000000 or next in blocked:
            return -1
        blocked.append(next)
        stage+=1
    return stage
maxloops=0

print(loop(220))
maxloopitems=[]
for i in range(2, 1000000):
    loops=loop(i)
    if loops>maxloops:
        maxloops=loops
        maxloopitems=[i]
        item=i
        for j in range(1, maxloops):
            item=d(item)
            maxloopitems.append(item)
        print(maxloops, maxloopitems)
print(loop(220))
