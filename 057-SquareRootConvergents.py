#Problem 57: It is possible to show that the square root of two can be expressed as an 
#infinite continued fraction. sqrt(2)=1+1/(2+1/(2+1/(2+....)) By expanding this for the 
#first four iterations, we get: 
"""
1+1/2=3/2=1.5 
1+1/(2+1/2)=7/5=1.4
1+1/(2+1/(2+1/2))=17/12=1.4166...
1+1/(2+1/(2+1/(2+1/2))=41/29=1.41379...
"""
#The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 
#1393/985, is the first example where the number of digits in the numerator exceeds the 
#number of digits in the denominator. In the first one-thousand expansions, how many 
#fractions contain a numerator with more digits than the denominator?

#1/(2+x/y)=1/(2y/y+x/y)=1/((2y+x)/y)=y/(2y+x)
limit=1000
roots=[]
numerator=1
denominator=2
while len(roots)<limit:
    #add prev answer in the denominator
    temp=denominator
    denominator=2*denominator+numerator
    numerator=temp
    #add one
    roots.append([numerator+denominator, denominator])

topHeavy=[]
for r in roots:
    if len(str(r[0]))>len(str(r[1])):
        print(r[0], "/", r[1])
        topHeavy.append(r)
print("Answer:", len(topHeavy))
