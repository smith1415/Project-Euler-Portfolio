#Problem 33: The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
#attempting to simplify it may incorrectly believe that 49/98=4/8, which is correct, is 
#obtained by cancelling the 9s. We shall consider fractions like, 30/50, to be trivial 
#examples. There are exactly four non-trivial examples of this type of fraction, less than one 
#in value, and containing two digits in the numerator and denominator. If the product of these 
#four fractions is given in its lowest common terms, find the value of the denominator.

list=[]
for a in range(1, 10):
    print(a)
    for b in range(a+1, 10):
        print("   ",b)
        for i in range(1, 10):
            ai=int(str(a)+str(i))
            bi=int(str(b)+str(i))
            ia=int(str(i)+str(a))
            ib=int(str(i)+str(b))
            if a/b==ai/bi:
                list.append([a, b, ai, bi])
                print(a, b, ai, bi)
            if a/b==ia/bi:
                list.append([a, b, ia, bi])
                print(a, b, ia, bi)
            if a/b==ai/ib:
                list.append([a, b, ai, ib])
                print(a, b, ai, ib)
            if a/b==ia/ib:
                list.append([a, b, ia, ib])
                print(a, b, ia, ib)
print(list)
product=1
for group in list:
    product*=group[0]
    product/=group[1]
print("Product:", product)
