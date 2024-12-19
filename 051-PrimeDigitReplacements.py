#Problem 51: By replacing the 1st digit of the 2-digit number *3, it turns out that six of 
#the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime. By replacing the 3rd 
#and 4th digits of 56**3 with the same digit, this 5-digit number is the first example 
#having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 
#56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this 
#family, is the smallest prime with this property. Find the smallest prime which, by 
#replacing part of the number (not necessarily adjacent digits) with the same digit, is 
#part of an eight prime value family.

booleans=[False, False]
for i in range(2, 1000001):
    booleans.append(True)

for i in range(2, 1000001):
    if booleans[i]:
        for j in range(2*i, 1000001, i):
            booleans[j]=False
primes=[]
for i in range(0, 1000000):
    if booleans[i]:
        primes.append(i)           

"""
These don't find any:
#four digit:
for f in range(1, 10):
    list=[]
    for m in range(0, 10):
        F=str(f)
        M=str(m)
        number=int(F+M+M+M)
        if(number in primes):
            list.append(number)
    print(f,"in 1 place",list)
for p in range(2, 5):
    for f in range(0, 10):
        list=[]
        for m in range(0, 10):
            F=str(f)
            M=str(m)
            if p==2:
                number=int(M+F+M+M)
            elif p==3:
                number=int(M+M+F+M)
            else:
                number=int(M+M+M+F)
            if(number in primes):
                list.append(number)
        print(f,"in", p, "place",list)

#five digit
for i in range(0, 10):
    for j in range(0, 10):
        for p in range(0, 5):
            for q in range(p+1, 5):
                list=[]
                for f in range(0, 10):
                    digits=[f, f, f, f, f]
                    digits[p]=i
                    digits[q]=j
                    number=""
                    for d in digits:
                        number+=str(d)
                    number=int(number)
                    if number in primes:
                        list.append(number)
                print(i,"in",str(p)+",", j,"in",q,list)
"""
finals=[]
#six digits
for i in range(0, 10):
    print(i)
    for j in range(0, 10):
        print("   ", j)
        for k in range(0,10):
            for p in range(0, 6):
                for q in range(p+1, 6):
                    for r in range(q+1, 6):
                        list=[]
                        for f in range(0, 10):
                            digits=[f, f, f, f, f, f]
                            digits[p]=i
                            digits[q]=j
                            digits[r]=k
                            number=""
                            for d in digits:
                                number+=str(d)
                            number=int(number)
                            if number in primes:
                                list.append(number)
                        if len(list)==8:
                            if list[0]>100000:
                                print("ANSWER:", list[0])
                            string=str(i)+" in "+str(p)+", "
                            string+=str(j)+" in "+str(q)+", "
                            string+=str(k)+" in "+str(r)
                            print(string, list)
