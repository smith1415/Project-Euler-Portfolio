#Problem 75: It turns out that 12cm is the smallest length of wire that can be bent to form an 
#integer sided right angle triangle in exactly one way, but there are many more examples.
"""
12cm: (3,4,5)
24cm: (6,8,10)
30cm: (5,12,13)
36cm: (9,12,15)
40cm: (8,15,17)
48cm: (12,16,20)
"""
#In contrast, some lengths of wire, like 20cm, cannot be bent to form an integer sided right angle 
#triangle, and other lengths allow more than one solution to be found; for example, using 120cm it 
#is possible to form exactly three different integer sided right angle triangles.
"""
120cm: (30,40,50), (20,48,52), (24,45,51)
"""
#Given that L is the length of the wire, for how many values of L can exactly one integer sided 
#right angle triangle be formed?

#a<b<c
#a^2+b^2=c^2
#a+b+c<=1500000
#(graphing y+x+sqrt(y^2+x^2)<=1500000 and y>x is a helpful visual)

#since b<c and a+b+c<=1500000
#if a is very small
#b:c -> 1:1
#b is 1/2 of the whole
#b<(1500000-a)/2
#b<750000-a/2


#since a<b<c and a+b+c<=1500000
#if b-a=very small
#a:b:c -> 1:1:sqrt(2)
#a is 1/(2+sqrt(2)) of the whole
#1500000/(2+sqrt(2))=439339.82822
#a<439340


#the list of pythagorean triples is optional and commented out
#triples=[]
sums=[]
for i in range(1, 439340):
    if i%10==0:
        print(i, len(sums))
    for j in range(i+1, 750000-int(i/2)):
        sum=i**2+j**2
        sqr=sum**(1/2)
        if sqr%1==0:
            sum=i+j+int(sqr)
            if sum<1500000:
                #print(i, j, int(sqr), sum)
                #triples.append([i, j, int(sqr), sum])
                if sum not in sums:
                    sums.append(sum)
#triples.sort()
#print("length", len(tripleSums))
print(sums)
#print(triples)
print("done!")
