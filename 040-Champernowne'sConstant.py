#Problem 40: An irrational decimal fraction is created by concatenating the positive integers: 0.123456789101112131415161718192021 It can be seen that the 12th digit of the fractional part is 1. If d<n> represents the nth digit of the fractional part, find the value of the following expression. d<1>*d<10>*d<100>*d<1000>*d<10000>*d<100000>*d<1000000>

def champerDigit(n):
    num=0
    digit=0
    while digit<n:
        num=num+1
        digit=digit+len(str(num))
    strnum=str(num)
    return int(strnum[n-digit-1])

product=1
d1=champerDigit(1)
print(d1)
product=product*d1
d10=champerDigit(10)
print(d10)
product=product*d10
d100=champerDigit(100)
print(d100)
product=product*d100
d1000=champerDigit(1000)
print(d1000)
product=product*d1000
d10000=champerDigit(10000)
print(d10000)
product=product*d10000
d100000=champerDigit(100000)
print(d100000)
product=product*d100000
d1000000=champerDigit(1000000)
print(d1000000)
product=product*d1000000

print("product:", product)

