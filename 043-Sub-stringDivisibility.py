#Problem 43: The number, 1406357289, is a 0 to 9 pandigital number because it is made up 
#of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-
#string divisibility property. Let d<1> be the 1st digit, d<2> be the 2nd digit, and so 
#on. In this way, we note the following: 
"""
d<2>d<3>d<4>=406 is divisible by 2 
d<3>d<4>d<5>=063 is divisible by 3
d<4>d<5>d<6>=635 is divisible by 5
d<5>d<6>d<7>=357 is divisible by 7
d<6>d<7>d<8>=572 is divisible by 11
d<7>d<8>d<9>=728 is divisible by 13
d<8>d<9>d<10>=289 is divisible by 17
"""
#Find the sum of all 0 to 9 pandigital numbers with this property.
divisible=[]
for a in range(0, 10):
    for b in range(0, 9):
        for c in range (0, 8):
            for d in range(0, 7):
                for e in range(0, 6):
                    for f in range(0, 5):
                        for g in range(0, 4):
                            for h in range(0, 3):
                                for i in range(0, 2):
                                    unusedDigits=[]
                                    for j in range(0, 10):
                                        unusedDigits.append(j)
                                    pandigital=""
                                    for sym in [a, b, c, d, e, f, g, h, i, 0]:
                                        pandigital=pandigital+str(unusedDigits[sym])
                                        unusedDigits.pop(sym)
                                    isDivisible=True
                                    divs=[1, 2, 3, 5, 7, 11, 13, 17]
                                    for i in range(1, 8):
                                        if int(pandigital[i:i+3])%divs[i]!=0:
                                            isDivisible=False
                                    if isDivisible:
                                        print(pandigital)
                                        divisible.append(int(pandigital))
sum=0
for d in divisible:
    sum=sum+d
print("sum:", sum)
