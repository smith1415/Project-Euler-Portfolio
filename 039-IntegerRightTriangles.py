#Problem 39: If p is the perimeter of a right angle triangle with integral length sides, 
#{a,b,c}, there are exactly three solutions for p=120. {20,48,52}, {24, 45, 51}, 
#{30, 40, 50} For which value of p<=1000, is the number of solutions maximised?

#p<=1000
#a+b+c<=1000
#a^2+b^2=c^2
list=[]
for i in range(0, 1000):
    list.append([])
for a in range(1, 334):
    for b in range(a, 501):
        c=(a**2+b**2)**(1/2)
        if c%1==0:
            if a+b+c<=1000:
                num=int(a+b+c)
                list[num-1].append([a, b, int(c)])
print(list)
maxLen=0
maxIndex=0
for i in range(0, len(list)):
    if len(list[i])>maxLen:
        maxLen=len(list[i])
        maxIndex=i
print(maxIndex+1, maxLen, list[maxIndex])
