#Problem 0: In a 1788 letter to a friend and teacher, Joseph Fourier wrote, "Here is a little problem of a rather singular nature: it occurred to me in connection with certain propositions in Euclid we discussed on several occasions. Arrage 17 lines in the same plane so that they give 101 points of interection. It is to be assumed that the lines extend to infinity, and that no point of intersection belongs to more than two lines" 
#After finding one solution (8, 4, 2, 1, 1), I took issue with the very concept that is was a question "singular in nature." I saw no reason why an arragement with 100 or 102 or 72 points of intersection would be any less interesting--unless of course there are some numbers for which it is impossible. Thus, I wrote this program to find all the numbers of intersections which are possible to make with 17 lines:

def recursion(n,lowest, goal):
    if n>goal:
        return 0
    if n==goal:
        return 1
    else:
        total=0
        for i in range (1, lowest+1):
            total=total+recursion(i, i, goal-n)
    return total

num=int(input("What number do you want to try?"))
print(str(recursion(0, num, num)))

def recursi(nums, goal):
    if sum(nums)>goal:
        return 0
    if sum(nums)==goal:
        print(nums)
        return 1
    total=0
    for i in range (1, nums[-1]+1):
        newnums=[]
        for n in nums:
            newnums.append(n)
        newnums.append(i)
        total=total+recursi(newnums, goal)
    return total


def groupings(num):
    out=0
    for i in range (1, num+1):
        out=out+recursi([i], num)
    return out

number=int(input("What number do you want to find the groupings of?"))
print(groupings(number))
