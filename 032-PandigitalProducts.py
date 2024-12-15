#Problem 32: We shall say that an n-digit number is pandigital if it makes use of all the digits 
#1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital. The 
#product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, 
#and product is 1 through 9 pandigital. Find the sum of all products whose 
#multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital. HINT: Some 
#products can be obtained in more than one way so be sure to only include it once in your sum.

#let d(x) return the number of digits in an integer x
#if x*y=z, then d(x)+d(y)>=d(z) 
#but also d(z)>=d(x) and d(z)>=d(y)
#if x, y, z is pandigital 1-9, then d(x)+d(y)+d(z)=9
#rearranged: d(z)=9-d(x)-d(y)
#thus all of these numbers satisfy the rules:
#d(x)+d(y)>=9-d(x)-d(y)  9-d(x)-d(y)>=d(x)  and 9-d(x)-d(y)>=d(y)
#if we graph these inequalities (and d(x)<=d(y)) and find the lattice points
#we will find the unique pairs of digits of our multiplicand and multiplier:
#[(1, 4), (2, 3), (3, 3)]

products=[]

#(1,4)
for A in range(0, 9):
    for a in range(0, 8):
        for b in range (0, 7):
            for c in range(0, 6):
                for d in range (0, 5):
                    unusedDigits=[]
                    for i in range(1, 10):
                        unusedDigits.append(str(i))
                    strmultiplicand=unusedDigits[A]
                    unusedDigits.pop(A)
                    strmultiplier=""
                    for letter in [a, b, c, d]:
                        strmultiplier=strmultiplier+unusedDigits[letter]
                        unusedDigits.pop(letter)
                    strproduct=str(int(strmultiplicand)*int(strmultiplier))
                    isSpanning=True
                    for digit in strproduct:
                        if digit not in unusedDigits:
                            isSpanning=False
                        else:
                            unusedDigits.remove(digit)
                    if isSpanning:
                        print(strmultiplicand,"*",strmultiplier, "=", strproduct)
                        if int(strproduct) not in products:
                            products.append(int(strproduct))
#(2, 3)
for A in range(0, 9):
    for B in range(0, 8):
        for a in range (0, 7):
            for b in range(0, 6):
                for c in range (0, 5):
                    unusedDigits=[]
                    for i in range(1, 10):
                        unusedDigits.append(str(i))
                    strmultiplicand=""
                    for letter in [A, B]:
                        strmultiplicand=strmultiplicand+unusedDigits[letter]
                        unusedDigits.pop(letter)
                    strmultiplier=""
                    for letter in [a, b, c]:
                        strmultiplier=strmultiplier+unusedDigits[letter]
                        unusedDigits.pop(letter)
                    strproduct=str(int(strmultiplicand)*int(strmultiplier))
                    isSpanning=True
                    for digit in strproduct:
                        if digit not in unusedDigits:
                            isSpanning=False
                        else:
                            unusedDigits.remove(digit)
                    if isSpanning:
                        print(strmultiplicand,"*",strmultiplier, "=", strproduct)
                        if int(strproduct) not in products:
                            products.append(int(strproduct))


#(3, 3)
for A in range(0, 9):
    for B in range(0, 8):
        for C in range (0, 7):
            for a in range(0, 6):
                for b in range(0, 5):
                    for c in range(0, 4):
                        unusedDigits=[]
                        for i in range(1, 10):
                            unusedDigits.append(str(i))
                        strmultiplicand=""
                        for letter in [A, B, C]:
                            strmultiplicand=strmultiplicand+unusedDigits[letter]
                            unusedDigits.pop(letter)
                        strmultiplier=""
                        for letter in [a, b, c]:
                            strmultiplier=strmultiplier+unusedDigits[letter]
                            unusedDigits.pop(letter)
                        strproduct=str(int(strmultiplicand)*int(strmultiplier))
                        isSpanning=True
                        for digit in strproduct:
                            if digit not in unusedDigits:
                                isSpanning=False
                            else:
                                unusedDigits.remove(digit)
                        if isSpanning:
                            print(strmultiplicand,"*",strmultiplier, "=", strproduct)
                            if int(strproduct) not in products:
                                products.append(int(strproduct))
print(products)
print(sum(products))
                    
