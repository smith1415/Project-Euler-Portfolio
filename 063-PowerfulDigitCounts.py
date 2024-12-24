#Problem 63: The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 
#134217728=8**9, is a ninth power. How many n-digit positive integers exist which are also an nth 
#power?

notFound=True
base=0
powers=[]
while notFound:
    base+=1
    exponent=0
    power=1
    while len(str(power))>=exponent:
        exponent+=1
        power=power*base
        if len(str(power))==exponent:
            powers.append([base, exponent, power])
    if base>8:
        print(powers)
        print(len(powers))
        notFound=False
