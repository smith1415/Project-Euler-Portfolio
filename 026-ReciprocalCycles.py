#have not solved (yet)
#Problem 26: A unit fraction contains 1 in the numerator. The decimal representation of 
#the unit fractions with denominators 2 to 10 are given:
#1/2=0.5
#1/3=0.(3)
#1/4=0.25
#1/5=0.2
#1/6=0.1(6)
#1/7=0.(142857)
#1/8=0.125
#1/9=0.(1)
#1/10=0.1
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 
#1/7 has a 6-digit recurring cycle. Find the value of d<1000 for which 1/d contains the 
#longest recurring cycle in its decimal fraction part.

def cycleScore(num):
    strnum=str(1/num)
    if len(strnum)<16:
        return 0
    else:
        guess=-1
        if num>100:
            strnum=str((10**18)/num)
        elif num>10:
            strnum=str((10**17)/num)
        else:
            strnum=str((10**16)/num)
        print(strnum)
        for i in range(0, 14):
            for j in range(i+1, 14):
                if strnum[i]==strnum[j]:
                    if strnum[i+1]==strnum[j+1]:
                        if strnum[i+2]==strnum[j+2]:
                            guess=j-i
                            break
        return guess

scores=[]
for i in range(1, 1001):
    scores.append(cycleScore(i))

mysterious=[]
max=0
maxIndex=0
for i in range(0, len(scores)):
    if scores[i]==-1:
        mysterious.append(i+1)
    if scores[i]>max:
        max=scores[i]
        maxIndex=i
print(max, maxIndex+1)
print(len(mysterious), mysterious)
