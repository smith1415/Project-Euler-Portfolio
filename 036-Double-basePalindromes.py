#Problem 36: The decimal number, 585=1001001001<2> (binary), is palindromic in both bases. Find the 
#sum of all numbers, less than one million, which are palindromic in base 10 and base 2. (Please 
#note that the palindromic number, in either base, may not include leading zeros.)

def isPalindrome(num):
    strnum=str(num)
    for i in range(0, len(strnum)):
        a=strnum[i]
        b=strnum[-1-i]
        if(not(a==b)):
            return False
    return True

def binary(num):
    power=1
    count=0
    while power<=num:
        power=power*2
        count=count+1
    out=""
    for i in range(0, count+1):
        if num>=2**(count-i):
            out=out+"1"
            num=num-2**(count-i)
        else:
            out=out+"0"
    return int(out)

doublebase=[]

#one digit:
for i in range(1, 10):
    num=i
    binum=binary(num)
    if isPalindrome(binum):
        doublebase.append(num)

#two digits:
for i in range(1, 10):
    num=int(str(i)+str(i))
    binum=binary(num)
    if isPalindrome(binum):
        doublebase.append(num)

#three digits:
for i in range(1, 10):
    for j in range(0, 10):
        num=int(str(i)+str(j)+str(i))
        binum=binary(num)
        if isPalindrome(binum):
            doublebase.append(num)

#four digits:
for i in range(1, 10):
    for j in range(0, 10):
        num=int(str(i)+str(j)+str(j)+str(i))
        binum=binary(num)
        if isPalindrome(binum):
            doublebase.append(num)

#five digits:
for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            num=int(str(i)+str(j)+str(k)+str(j)+str(i))
            binum=binary(num)
            if isPalindrome(binum):
                doublebase.append(num)

#six digits:
for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            num=int(str(i)+str(j)+str(k)+str(k)+str(j)+str(i))
            binum=binary(num)
            if isPalindrome(binum):
                doublebase.append(num)

print(doublebase)

sum=0
for n in doublebase:
    sum=sum+n
print(sum)
