#Problem 76: It is possible to write five as a sum in exactly six different ways:
"""
4+1
3+2
3+1+1
2+2+1
2+1+1+1
1+1+1+1+1
"""
#How many different ways can one hundred be written as a sum of at least two positive integers?

#see problem 0 
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

num=int(input("What number do you want to try?"))
ans=ways(0, num, num)
print(ans)
print("only sums:", ans-1)
