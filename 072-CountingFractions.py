#have not solved (yet)
#Problem 72: Consider the fraction, n/d, where n and d are positive integers. If n<d and 
#HCF(n,d)=1, it is called a reduced proper fraction. If we list the set of reduced proper 
#fractions for in ascending order of size, we get:
"""
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
"""
#It can be seen that there are 21 elements in this set. How many elements would be 
#contained in the set of reduced proper fractions for d<=1000000?

def totient(num):
    list=[]
    for i in range(0, num):
        list.append(i)
    for i in range(2, num):
        item=list[i]
        if not item==num+1:
            if num%item==0:
                multiple=item
                while multiple<num:
                    list[multiple]=num+1
                    multiple=multiple+item
    while num+1 in list:
        list.remove(num+1)
    return len(list)-1
sum=0
for i in range(2, 1000000):
    sum+=totient(i)
    if i%100==0:
        print(i, sum)
print("answer", sum)
