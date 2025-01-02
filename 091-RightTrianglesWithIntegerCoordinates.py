#have not solved (yet)
#Problem 91: The points P(x<1>, y<1>) and Q(x<2>, y<2>) are plotted at integer co-ordinates and 
#are joined to the origin, O(0,0), to form triOPQ.
#<picture of OPQ>
#There are exactly fourteen triangles containing a right angle that can be formed when each 
#co-ordinate lies between 0 and 2 inclusive; that is, 0 <= x<1>, y<1>, x<2>, y<2> <= 2.
#<picture of all 14>
#Given that 0 <= x<1>, y<1>, x<2>, y<2> <= 50, how many right triangles can be formed?

#see problem 85
#for an a x b grid, there are 1/4(a^2+a)(b^2+b) rectangles which can be formed
#R(a,b)=1/4(a^2+a)(b^2+b)
#This is a similar problem. However, right triangles can have irrational lengths
#also one the points is at the origin now. hmmm

#Attempt 1 
"""
triangles=[]
for x in range(1, 50):
    for y in range(1, 50):
        triangles.append([[0, 0], [x, 0], [0, y]])
        triangles.append([[0, 0], [x, y], [0, y]])
        triangles.append([[0, 0], [x, 0], [x, y]])
for x in range(2, 50, 2):
    y=int(x/2)
    triangles.append([[0,0], [y, y], [x, 0]])
    triangles.append([[0,0], [y, y], [0, x]])

print(len(triangles))
"""
#more complicated than I thought...
