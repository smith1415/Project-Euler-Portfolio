#Problem 71: Consider the fraction, n/d, where n and d are positive integers. If n<d and 
#HCF(n,d)=1, it is called a reduced proper fraction. If we list the set of reduced proper 
#fractions for in ascending order of size, we get:
"""
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
"""
#It can be seen that 2/5 is the fraction immediately to the left of 3/7. By listing the set of 
#reduced proper fractions for d<=1000000 in ascending order of size, find the numerator of the 
#fraction immediately to the left of 3/7.

def totientList(num):
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
    list.remove(0)
    return list

def binarySearch(f, item, min, max):
    if max>=min:
        i=int((min+max)/2)
        if f[i-1][0]/f[i-1][1]<item:
            if f[i][0]/f[i][1]>item:
                return i
            else:
                return binarySearch(f, item, i+1, max)
        else:
            return binarySearch(f, item, min, i-1)
    else:
        return -1
    

num=int(input("What numerator?"))
denom=int(input("What denominator?"))
frac=[num, denom]


fractions=[[1, 2]]
for i in range(3, 1000000):
    for t in totientList(i):
        f=[t, i]
        fr=t/i
        if fractions[-1][0]/fractions[-1][1]<fr:
            fractions.append(f)
        if fractions[0][0]/fractions[0][1]>fr:
            fractions.insert(0, f)
        else:
            fractions.insert(binarySearch(fractions, fr, 0, len(fractions)), f)
    if i>denom and i%100==0:
        print(i)
        index=fractions.index(frac)
        print(fractions[index-1], fractions[index])
      
