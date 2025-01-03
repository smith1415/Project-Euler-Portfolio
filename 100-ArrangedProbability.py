#have not solved (yet)
#Problem 100: If a box contains twenty-one coloured discs, composed of fifteen blue discs 
#and six red discs, and two discs were taken at random, it can be seen that the probability 
#of taking two blue discs, P(BB)=(15/21)*(14/20)=1/2. The next such arrangement, for which 
#there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-
#five blue discs and thirty-five red discs. By finding the first arrangement to contain over 
#10**12=1 000 000 000 000 discs in total, determine the number of blue discs that the box 
#would contain.

#let x=total num of discs 
#let y=num of blue discs
#y/x*(y-1)/(x-1)=1/2 for what integer values of x and y?
#y(y-1)=x(x-1)/2
#y=sqrt((x^2-x+1/2)/2)+1/2

"""Attempt 1:
notFound=True
discs=10**12
while notFound:
    blues=((discs**2-discs+1/2)/2)**(1/2)+1/2
    if blues%1==0:
        n=blues*(blues-1)
        d=discs*(discs-1)
        total=n/d
        print("DISCS", discs, "BLUES", blues, "CHANCE", total)
        if discs>10**13 and total==1/2:
            notFound=False
    discs=discs+1

decimals are not exact enough :(
I need to prime factor"""

