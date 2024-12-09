#Problem 25: The Fibonacci sequence is defined by the recurrence relation: Fn=Fn-1+Fn-2, 
#where F1=1 and F2=1. Hence the first 12 terms will be: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 
#89, 144. The 12th term, F12, is the first term to contain three digits. What is the index 
#of the first term in the Fibonacci sequence to contain 1000 digits?

fibonacciNumbers=[]
num1=1
num2=1
while num2<10**1000:
    fibonacciNumbers.append(num1)
    fibonacciNumbers.append(num2)
    num1=num1+num2
    num2=num1+num2
print(len(fibonacciNumbers))
for i in range(1,len(fibonacciNumbers)+1):
    print(len(str(fibonacciNumbers[len(fibonacciNumbers)-i])))
