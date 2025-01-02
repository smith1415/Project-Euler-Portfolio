#have not solved (yet)
#(When ran this on my computer, it broke, and I had to replace the motherboard...)
#Problem 92: A number chain is created by continuously adding the square of the digits in a 
#number to form a new number until it has been seen before.
"""
For example,
44->32->13->10->1->1
85->89->145->42->20->4->16->37->58->89
"""
#Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is 
#most amazing is that EVERY starting number will eventually arrive at 1 or 89. How many 
#starting numbers below ten million will arrive at 89?

list89=[89]
list1=[1]

def chain89(n):
    sum=0
    num=n
    while num>0:
        digit=num%10
        sum=sum+digit**2
        num=int(num/10)
    if sum in list89:
        list89.append(n)
        return True
    elif sum in list1:
        list1.append(n)
        return False
    else:
        return chain89(sum)

total=0
for t in range(1, 1001):
    for i in range((t-1)*10000+1, t*10000+1):
        if chain89(i):
            total+=1
    print(str(t/10)+"%", total)
