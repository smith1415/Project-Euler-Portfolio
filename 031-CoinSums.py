#Problem 31: In the United Kingdom the currency is made up of pound (£) and pence (p). 
#There are eight coins in general circulation: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 
#(200p). It is possible to make £2 in the following way: 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p. How many different ways can £2 be made using any number of coins?

#just finds the number of ways regularly (see #0 or #76)
def recursion(n, lowest, goal):
    if n>goal:
        return 0
    if n==goal:
        return 1
    else:
        total=0
        for i in range(1, lowest+1):
            total=total+recursion(i, i, goal-n)
    return total

#finds the list of ways regularly
def recursi(nums, goal):
    if sum(nums)>goal:
        return 0
    if sum(nums)==goal:
        list.append(nums)
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

#based on those I made these:
#finds the number of ways only using coin values
def coinRecursion(n, lowest, goal):
    if n>goal:
        return 0
    if n==goal:
        return 1
    else:
        list=[1, 2, 5, 10, 20, 50, 100, 200]
        i=0
        total=0
        while not(i==len(list)) and list[i]<=lowest:
            total=total+coinRecursion(list[i], list[i], goal-n)
            i+=1
    return total


#finds the list of ways
def coinRecursi(nums, goal, finalList):
    if sum(nums)>goal:
        return 0
    if sum(nums)==goal:
        finalList.append(nums)
        return 1
    else:
        list=[1, 2, 5, 10, 20, 50, 100, 200]
        i=0
        total=0
        while not(i==len(list)) and list[i]<=nums[-1]:
            newnums=[]
            for n in nums:
                newnums.append(n)
            newnums.append(list[i])
            total=total+coinRecursi(newnums, goal, finalList)
            i+=1
        return total
def coinGroupings(num, listing):
    out=0
    for i in [1, 2, 5, 10, 20, 50, 100, 200]:
        out=out+coinRecursi([i], num, listing)
    return out


print("simple way:", coinRecursion(0, 200, 200))

groups=[]
print("complicated way:", coinGroupings(200, groups))
print(len(groups))
for group in groups:
    print(group)
