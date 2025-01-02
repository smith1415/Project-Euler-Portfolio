#have not solved (yet)
#Problem 86: A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a 
#fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest 
#"straight line" distance from S to F is 10 and the path is shown on the diagram. However, 
#there are up to three "shortest" path candidates for any given cuboid and the shortest route 
#doesn't always have integer length. It can be shown that there are exactly 2060 distinct 
#cuboids, ignoring rotations, with integer dimensions, up to a maximum size of M by M by M, for 
#which the shortest route has integer length when M=100. This is the least value of M for which 
#the number of solutions first exceeds two thousand; the number of solutions when M=99 is 1975. 
#Find the least value of M such that the number of solutions first exceeds one million.

def numSums(n, exclude):
    output=int(n/2)
    return output


abcList=[]
cuboid=[]
M=100
for i in range(1, M):
    for j in range(i, M):
        sum=i**2+j**2
        sqr=sum**(1/2)
        if sqr%1==0:
            abcList.append([i, j, int(sqr)])
for triple in abcList:
    for i in range (1, int(triple[0]/2+1)):
        cuboid.append([i, triple[0]-i, triple[1]])
print(len(cuboid))
