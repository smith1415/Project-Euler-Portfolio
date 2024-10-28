#Problem 4:A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009=91*99. Find the largest palindrome made from the product of two 3-digit numbers.

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

nums=[]
for i in range(100, 1000):
    for j in range(i, 1000):
        c=i*j
        nums.append(c)

candidates=[]
for n in nums:
    if isPalindrome(n):
        candidates.append(n)

largest=candidates[-1]
for n in candidates:
    if n>largest:
        largest=n

print("largest:", largest)
print(candidates)
