#Problem 56: A googol (10**100) is a massive number: one followed by one-hundred zeros; 
#100**100 is almost unimaginably large: one followed by two-hundred zeros. Despite their 
#size, the sum of the digits in each number is only 1. Considering natural numbers of the 
#form, a**b, where a,b<100, what is the maximum digital sum?

max=[1, 1]
maxsum=1
for i in range(1, 101):
    for j in range(1, 101):
        pow=i**j
        strpow=str(pow)
        sum=0
        for digit in strpow:
            sum=sum+int(digit)
            if maxsum<sum:
                maxsum=sum
                max=[i, j]
print(max[0], "**", max[1], "=", max[0]**max[1], "   sum:", maxsum)
