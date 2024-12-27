#Note:I call this program "problem 0." It truly is not a project Euler problem, or if it 
#is, it is not indexed at 0. However, solving this problem led me to discover Project 
#Euler. At the end of last summer, I spent a entire afternoon staring at this program 
#and figuring out what I wanted it to do. After finding the solution, I told my friends 
#about it and one of them told me about Project Euler, so this problem started it all.

#Problem 0: In a 1788 letter to a friend and teacher, Joseph Fourier wrote, "Here is a 
#little problem of a rather singular nature: it occurred to me in connection with 
#certain propositions in Euclid we discussed on several occasions. Arrage 17 lines in 
#the same plane so that they give 101 points of interection. It is to be assumed that 
#the lines extend to infinity, and that no point of intersection belongs to more than 
#two lines" 

#After finding one solution (8, 4, 2, 1, 1), I took issue with the idea that this is 
#a question "singular in nature." I saw no reason why an arragement with 100 or 102 or 
#72 points of intersection would be any less interesting--unless of course there are 
#some numbers for which it is impossible. Thus, I wrote this program to find all the 
#numbers of intersections which are possible to make with 17 lines:

#simply counts the number of ways to group the lines into sets of parallels
def ways(n,lowest, goal):
    if n>goal:
        return 0
    if n==goal:
        return 1
    else:
        total=0
        for i in range (1, lowest+1):
            total=total+ways(i, i, goal-n)
    return total
num=int(input("How many lines?"))
print("This is the number of different groupings:"+str(ways(0, num, num)))

#gives a list of the different ways
def listWays(nums, goal):
    if sum(nums)>goal:
        return 0
    if sum(nums)==goal:
        list.append(nums)
        return 1
    total=0
    for i in range(1, nums[-1]+1):
        newnums=[]
        for n in nums:
            newnums.append(n)
        newnums.append(i)
        total=total+listWays(newnums, goal)
    return total
def groupings(n):
    out=0
    for i in range (1, n+1):
        out=out+listWays([i], n)
    return out

list=[]
temp=input("Press enter if you want to see the groupings")
print(groupings(num))
for i in list:
    print(i)


#goes further and gives the intersections of lines in those groupings
temp=input("Press enter if you want to see the number of intersections of these groupings")
Xs=[]
for group in list:
    intersections=int(num*(num-1)/2)
    for g in group:
        lostIntersections=int(g*(g-1)/2)
        intersections=intersections-lostIntersections
    Xs.append([intersections, group])
Xs.sort()
for item in Xs:
    print(item[0], item[1])
