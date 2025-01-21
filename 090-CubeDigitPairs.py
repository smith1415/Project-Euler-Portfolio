#Problem 90: Each of the six faces on a cube has a different digit (0 to 9) written on it; 
#the same is done to a second cube. By placing the two cubes side-by-side in different 
#positions we can form a variety of 2-digit numbers. For example, the square number 64 
#could be formed: 
<picture of cube with 6 on front face beside cube with 4 on front face>
#In fact, by carefully choosing the digits on both cubes it is possible to display all of 
#the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81. For 
#example, one way this can be achieved is by placing {0,5,6,7,8,9} on one cube and 
#{1,2,3,4,8,9} on the other cube. However, for this problem we shall allow the 6 or 9 to 
#be turned upside-down so that an arrangement like {0,5,6,7,8,9} and {1,2,3,4,8,9} allows 
#for all nine square numbers to be displayed; otherwise it would be impossible to obtain 
#09. In determining a distinct arrangement we are interested in the digits on each cube, 
#not the order. 
"""
{1,2,3,4,5,6} is equivalent to {3,6,4,1,2,5}
{1,2,3,4,5,6} is distinct from {1,2,3,4,5,9}
"""
#But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last 
#example both represent the extended set {1,2,3,4,5,6,9} for the purpose of forming 2-
#digit numbers. How many distinct arrangements of the two cubes allow for all of the 
#square numbers to be displayed?

def containsAllPairs(L1, L2, pairList):
    for p in pairList:
        if not((p[0] in L1 and p[1] in L2) or (p[0] in L2 and p[1] in L1)):
            return False
    return True

#all nines are sixes to address the flipping property
digits=[[0, 1], [0,4], [0,6], [1, 6], 
        [2,5], [3, 6], [4,6], [6, 4], [8,1]]

c1list=[]
c2list=[]

list1=[1, 2, 3, 4, 5, 6, 7, 8, 6]
list2=[2, 3, 4, 5, 6, 7, 8, 6]

for a in range(0, 5):
    for b in range(a+1, 6):
        for c in range(b+1, 7):
            for d in range(c+1, 8):
                for e in range(d+1, 9):
                    cube1=[0]
                    for letter in[a, b, c, d, e]:
                        cube1.append(list1[letter])
                    c1list.append(cube1)

for a in range(0, 5):
    for b in range(a+1, 6):
        for c in range(b+1, 7):
            for d in range(c+1, 8):
                cube2=[0,1]
                for letter in[a, b, c, d]:
                    cube2.append(list2[letter])
                c2list.append(cube2)
for a in range(0, 4):
    for b in range(a+1, 5):
        for c in range(b+1, 6):
            for d in range(c+1, 7):
                for e in range(d+1, 8):
                    cube2=[1]
                    for letter in[a, b, c, d, e]:
                        cube2.append(list2[letter])
                    c2list.append(cube2)

finalList=[]
for c1 in c1list:
    for c2 in c2list:
        if containsAllPairs(c1, c2, digits):
            if [c2, c1] not in finalList:
                finalList.append([c1, c2])
print(len(finalList))
