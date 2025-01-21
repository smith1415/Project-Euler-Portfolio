#Problem 34: 145 is a curious number, as 1!+4!+5!=145. Find the sum of all numbers which 
#are equal to the sum of the factorial of their digits. Note: As 1!=1 and 2!=2 are not 
#sums they are not included.

def factorial(num):
    product=1
    for i in range(1, num+1):
        product=product*i
    return product


digitFactorials=[]
for i in range(10, 100000):
    stri=str(i)
    sum=0
    for letter in stri:
        sum=sum+factorial(int(letter))
    if sum==i:
        digitFactorials.append(i)
print(digitFactorials)
sum=0
for item in digitFactorials:
    sum+=item
print(sum)
