#Problem 21:Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
#which divide evenly into n). If d(a)=b and d(b)=a, where a!=b, then a and b are an 
#amicable pair and each of a and b are called amicable numbers. For example, the proper 
#divisors of 220 are 1,2,4,5,10,11,20,22,44,55, and 110; therefore d(220)=284. The proper 
#divisors of 284 are 1,2,4,71, and 142; so d(284)=220. Evaluate the sum of all the amicable 
#numbers under 10000.

def d(num):
    if num==0 or num==1:
        return 0
    if num==2 or num==3:
        return 1
    else:
        sum=1
        for i in range(2,int(num**(1/2)+1)):
            if(num%i==0):
                sum=sum+i
                if(not(int(num/i)==i)):
                    sum=sum+int(num/i)
    return sum

num=int(input("Up to what number?"))
list=[]
for i in range(0, num+1):
    list.append([i, d(i)])

sum=0
for pair in list:
    if pair[1]>pair[0] and pair[1]<num:
        if list[pair[1]][1]==pair[0]:
            sum=sum+pair[0]
            print(pair[0])
            sum=sum+pair[1]
            print(pair[1])
print(sum)
