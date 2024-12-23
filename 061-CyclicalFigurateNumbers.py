#have not solved (yet)
#Problem 61: Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all 
#figurate (polygonal) numbers and are generated by the following formulae:
"""
Triangle    P<3,n>=n(n+1)/2   1,3,6,10,15,...
Square      P<4,n>=n**2       1,4,9,16,25,...
Pentagonal	P<5,n>=n(3n-1)/2  1,5,12,22,35,...
Hexagonal   P<6,n>=n(2n-1)    1,6,15,28,45,...
Heptagonal	P<7,n>=n(5n-3)/2  1,7,18,34,55,... 	
Octagonal	 	P<8,n>=n(3n-2)    1,8,21,40,65,...
"""
#The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties. 
#1. The set is cyclic, in that the last two digits of each number is the first two digits of the 
#next number (including the last number with the first). 
#2. Each polygonal type: triangle (P<3,127>=8128), square (P<4,91>=8281), and pentagonal 
#(P<5,44>=2882), is represented by a different number in the set.
#3. This is the only set of 4-digit numbers with this property.
#Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: 
#triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different 
#number in the set.

#Here's some helpful code from Problem 45:
def sqrt(num):
    return num**(1/2)

def invP(num):
    return sqrt(2/3*num+1/36)+1/6

def invH(num):
    return sqrt(t/2+1/16)+1/4

t=40755
i=285
print("Given Triangle Number:", t)

notFound=True
while notFound:
    i+=1
    t+=i
    Pn=invP(t)
    if Pn==int(Pn):
        Hn=invH(t)
        if Hn==int(Hn):
            print("Next Triangle Number:", t)
            notFound=False
