#have not solved (yet)
#Problem 60: The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property. Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

#I tried to go larger and it cause a memory error :(
searchWindow=100000000
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

bigPrimes=[]
for i in range(primes.index(7), primes.index(99991)):
    bigPrimes.append(primes[i])

array=[3, 7]
"""levelOne=[]
for b in bigPrimes:
    winner=True
    for a in array:
        if int(str(a)+str(b)) not in primes:
            winner=False
        if int(str(b)+str(a)) not in primes:
            winner=False
    if winner:
        levelOne.append(b)
print(levelOne)"""

#found in previous run:
levelOne=[109, 229, 541, 673, 823, 1237, 2503, 2707, 4159, 4729, 5521, 9901, 10459, 10627, 14851, 15313, 19183, 19237, 20899, 21397, 22921, 24517, 24847, 25189, 27823, 29059, 29587, 29761, 29947, 34057, 38791, 41227, 41641, 48889, 51061, 51133, 54037, 54973, 55171, 56533, 58573, 60649, 61357, 61363, 61441, 61927, 62233, 65257, 65293, 71971, 73063, 74047, 74317, 76099, 76819, 76837, 77617, 79579, 79693, 80917, 82231, 83023, 84697, 90199, 91009, 91159, 93187, 94201, 94327, 96181, 97549]
print(levelOne)

pairs=[]
for a in range(0, len(levelOne)):
    for b in range(a+1, len(levelOne)):
        winner=True
        if int(str(levelOne[a])+str(levelOne[b])) not in primes:
            winner=False
        if int(str(levelOne[b])+str(levelOne[a])) not in primes:
            winner=False
        if winner:
            pairs.append([a,b])
            print(a,b)
print(pairs)
