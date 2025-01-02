#have not solved (yet)
#Problem 78 Let p(n) represent the number of different ways in which n coins can be separated 
#into piles. For example, five coins can be separated into piles in exactly seven different 
#ways, so p(5)=7.
"""
OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
"""
#Find the least value of n for which p(n) is divisible by one million.

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

num=0
ans=1
while not ans%1000000==0:
    print(num)
    num+=1
    ans=recursion(0, num, num)
print(num, ans)
