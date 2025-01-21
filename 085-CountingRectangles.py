#Problem 85: By counting carefully it can be seen that a rectangular grid measuring 3 by 2
#contains eighteen rectangles:
"""
6: 1x1
4: 2x1
2: 3x1
3: 1x2
2: 2x2
1: 3x2
"""
#Although there exists no rectangular grid that contains exactly two million rectangles, 
#find the area of the grid with the nearest solution.

#This problem can be explored with a two variable (length and width) function. 

#That function was on the HCSSiM 2024 Interesting test! I've already found it!
#I did a visual proof on paper, but here I'll just put my findings:
#For an a x b grid, there are 1/4(a^2+a)(b^2+b) rectangles which can be formed.

#we need the integers a and b where 1/4(a^2+a)(b^2+b) is closest to 2 million
#That's only a two variable equation. let's graph it!
#1/4(x^2+x)(y^2+y)=2000000
#Isolate y to get:
#sqrt(8000000/(x^2+x)+0.25)+0.5

lower=[]
upper=[]
for x in range(5, 54):
    y=(8000000/(x**2+x)+0.25)**0.5-0.5
    lower.append([x, int(y)])
    upper.append([x, int(y+1)])

closestLeft=lower[0]
clDiff=2000000
clRect=0
for pair in lower:
    rectangles=1/4*(pair[0]**2+pair[0])*(pair[1]**2+pair[1])
    diff=2000000-rectangles
    if diff<clDiff:
        closestLeft=[pair[0], pair[1]]
        clDiff=diff
        clRect=rectangles

closestRight=upper[0]
crDiff=2000000
crRect=0
for pair in upper:
    rectangles=1/4*(pair[0]**2+pair[0])*(pair[1]**2+pair[1])
    diff=rectangles-2000000
    if diff<crDiff:
        closestRight=[pair[0], pair[1]]
        crDiff=diff
        crRect=rectangles

if clDiff<crDiff:
    print(closestLeft, clDiff, clRect)
    print(closestLeft[0]*closestLeft[1])
else:
    print(closestRight, crDiff, crRect)
    print(closestRight[0]*closestRight[1])
