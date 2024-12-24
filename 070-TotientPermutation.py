#have not solved (yet)
#Problem 70: Euler's totient function, phi(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1,2,4,5,7, and 8, are all less than nine and relatively prime to nine, phi(9)=6. The number 1 is considered to be relatively prime to every positive number, so phi(1)=1. Interestingly, phi(87109)=79180, and it can be seen that 87109 is a permutation of 79180. Find the value of n, 1<n<10**7, for which phi(n) is a permutation of n and the ratio n/phi(n) produces a minimum.

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
def totient(num):
    list=[]
    for i in range(0, num):
        list.append(i)
    for i in range(2, num):
        item=list[i]
        if not item==num+1:
            if num%item==0:
                multiple=item
                while multiple<num:
                    list[multiple]=num+1
                    multiple=multiple+item
    while num+1 in list:
        list.remove(num+1)
    return len(list)-1

minRatio=100
coolestNum=1
list=[]
for i in range(1, 2311, 2):
    list.append(i)
for i in range(3, 2311, 6):
    list.remove(i)
for i in range(5, 2311, 30):
    list.remove(i)
    list.remove(i+20)
for i in range(7, 2311, 210):
    list.remove(i)
    list.remove(i+42)
for i in range(11, 2311, 2310):
    list.remove(i)
    list.remove(i+110)
list.remove(1)
list.append(2311)
#10**7/2310=432
for round in range(0, 4330):
    print(round)
    for item in list:
        i=item+2310*round
        t=totient(i)
        r=i/t
        if minRatio>r:
            if arePermutations(i,t):
                coolestNum=i
                minRatio=r
                print(i, t, r)
        if i%100000==0:
            print(int(i/100000))
print("Coolest Number:", coolestNum)
