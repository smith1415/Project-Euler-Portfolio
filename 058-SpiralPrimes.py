#have not solved (yet)
#Problem 58: Starting with 1 and spiralling anticlockwise in the following way, a square 
#spiral with side length 7 is formed.
"""
37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49
"""
#It is interesting to note that the odd squares lie along the bottom right diagonal, but 
#what is more interesting is that 8 out of the 13 numbers lying along both diagonals are 
#prime; that is, a ratio of 8/13=62%. If one complete new layer is wrapped around the 
#spiral above, a square spiral with side length 9 will be formed. If this process is 
#continued, what is the side length of the square spiral for which the ratio of primes 
#along both diagonals first falls below 10%?

notFound=True
#2**20
searchWindow=1048576
pd=[3,5,7] #prime diagonals
cd=[9] #composite diagonals
num=9
inc=2
ratio=1
while notFound:
    print(searchWindow)
    booleans=[False, False]
    for i in range(2, searchWindow):
        booleans.append(True)
    
    for i in range(2, searchWindow):
        if booleans[i]:
            for j in range(2*i, searchWindow, i):
                booleans[j]=False
    primes=[]
    for i in range(0, searchWindow):
        if booleans[i]:
            primes.append(i)  
    print("primes found")

    while len(pd)/len(cd)>0.1 and cd[-1]<searchWindow:
        ratio=len(pd)/len(cd)
        inc+=2
        if inc%100==0:
            print("   ",inc)
        for i in range(0,4):
            num+=inc
            if num in primes:
                pd.append(num)
            else:
                cd.append(num)
    if len(pd)/len(cd)<=0.1:
        print(pd)
        print(cd)
        print(ratio)
        print(inc+1)
        notFound=False
    print(ratio)
    searchWindow*=2
