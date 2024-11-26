#Problem 9:A Pythagorean triplet is a set of three natural numbers, a<b<c, for which, 
#a^2+b^2=c^2. For example, 3^2+4^2=9+16=25=5^2. There exists exactly one Pythagorean 
#triplet for which a+b+c=1000. Find the product abc.

num = int(input("What number is the sum of the Pythagorean triplet?"))
abcList=[]
for i in range(1, num):
    for j in range(i, num):
        sum=i**2+j**2
        sqr=sum**(1/2)
        if sqr%1==0:
            abcList.append([i, j, int(sqr)])
for triple in abcList:
    sum=triple[0]+triple[1]+triple[2]
    if num==sum:
        print("Triple:", triple[0], triple[1], triple[2])
        print("Product:", triple[0]*triple[1]*triple[2])
