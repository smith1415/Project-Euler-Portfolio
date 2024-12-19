#Problem 52: It can be seen that the number, 1257874, and its double, 251748, contain 
#exactly the same digits, but in a different order. Find the smallest positive integer, x, 
#such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def arePermutations(a, b):
    stra=str(a)
    strb=str(b)
    digits=[]
    for digit in stra:
        digits.append(digit)
    for digit in strb:
        if digit in digits:
            digits.remove(digit)
        else:
            return False
    if digits==[]:
        return True
    else:
        return False

notFound=True
i=0
while notFound:
    i+=1
    limit=1
    if arePermutations(i, 2*i):
        limit=2
        if arePermutations(i, 3*i):
            limit=3
            if arePermutations(i, 4*i):
                limit=4
                if arePermutations(i, 5*i):
                    limit=5
                    if arePermutations(i, 6*i):
                        limit=6
                        print("FOUND", i, 2*i, 3*i, 4*i, 5*i, 6*i)
                        notFound=False
    if limit>1:
        print(limit)
