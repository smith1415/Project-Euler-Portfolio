#Problem 53: There are exactly ten ways of selecting three from five, 12345: 123, 124, 125, 
#134, 135, 145, 234, 235, 245, and 345. In combinatorics, we use the notation, (5-3)=10. In 
#general, (n-r)=n!/(r!(n-r)!), where r<=n, n!=n*(n-1)*...*3*2*1, and 0!=1. It is not until 
#n=23, that a value exceeds one-million: (23-10)=1144066. How many, not necessarily 
#distinct, values of (n-r) for 1<=n<=100, are greater than one-million?

def fac(num):
    product=1
    for i in range(1, num+1):
        product=product*i
    return product

count=0
for i in range(23, 101):
    for j in range(2, i):
        choose=fac(i)/(fac(j)*fac(i-j))
        if choose>1000000:
            count+=1
print(count)
