#Problem 20: n! means n x (n-1) x ... x 3 x 2 x 1. For example, 
#10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800, and the sum of the digits in the 
#number 10! is 3+6+2+8+8+0+0=27. Find the sum of the digits in the number 100!.

def factorial(num):
    product=1
    for i in range(1, num+1):
        product=product*i
    return product

num=int(input("What number do you want to use?"))
torial=factorial(num)
print(torial)
strial=str(torial)
sum=0
for i in range(0, len(strial)):
    sum=sum+int(strial[i])
print(sum)
