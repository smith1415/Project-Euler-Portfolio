#Problem 55: If we take 47, reverse and add, 47+74=121, which is palindromic. Not all 
#numbers produce palindromes so quickly. 
#For example, 1. 349+943=1292  2. 1292+2921 3. 4213+3124=7337. That is, 349 took three 
#iterations to arrive at a palindrome. Although no one has proved it yet, it is thought 
#that some numbers, like 196, never produce a palindrome. A number that never forms a 
#palindrome through the reverse and add process is called a Lychrel number. Due to the 
#theoretical nature of these numbers, and for the purpose of this problem, we shall assume 
#that a number is Lychrel until proven otherwise. In addition you are given that for every 
#number below ten-thousand, it will either (i) become a palindrome in less than fifty 
#iterations, or, (ii) no one, with all the computing power that exists, has managed so far 
#to map it to a palindrome. In fact, 10677 is the first number to be shown to require over 
#fifty iterations before producing a palindrome: 4668731596684224899951378664 (53 
#iterations, 28-digits). Surprisingly, there are palindromic numbers that are themselves 
#Lychrel numbers; the first example is 4994. How many Lychrel numbers are there below 
#ten-thousand?
#NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature 
#of Lychrel numbers.

def isPalindrome(num):
    length=0
    n=num
    while n>=1:
        length+=1
        n=n/10

    for i in range(0, length):
        a=int((num%(10**(length-i)))/(10**(length-i-1)))
        b=int((num%(10**(i+1)))/(10**i))
        if(not(a==b)):
            return False
    return True

def revadd(num):
    n=num
    rev=n%10
    n=int(n/10)
    while n>0:
        rev=rev*10
        rev=rev+n%10
        n=int(n/10)
    output=num+rev
    return output

def cycles(num, level):
    num=revadd(num)
    if isPalindrome(num):
        return level
    elif level>=50:
        return -1
    else:
        return cycles(num, level+1)
        
lycrel=[]
for i in range(1, 10000):
    v=cycles(i, 0)
    if v==-1:
        lycrel.append(i)

print("length:", len(lycrel), lycrel)
