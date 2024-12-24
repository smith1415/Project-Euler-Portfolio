#Problem 74: The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145: 1!+4!+5!=1+24+120=145. Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist: 
"""
169->363601->1454->169
871->45361->871
871->45362->872
"""
#It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
"""
69->363600->1454->169->363601(->1454)
78->45360->871->45361(->871)
540->145(->145)
"""
#Starting with 60 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms. How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

def factorial(num):
    product=1
    for i in range(2, num+1):
        product*=i
    return product

#digit factorial sum (dfs)
def dfs(num):
    sum=0
    while num>0:
        d=num%10
        sum=sum+factorial(d)
        num=int(num/10)
    return sum

counterIs60=[]
for i in range(1, 1000000):
    prev=[]
    counter=0
    curr=i
    while curr not in prev:
        prev.append(curr)
        curr=dfs(curr)
        counter+=1
    if counter==60:
        counterIs60.append(i)
        print(i)
print(len(counterIs60))
print(counterIs60)
        
