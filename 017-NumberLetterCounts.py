#Problem 17: If the numbers 1 to 5 are written out in words: one, two, three, four, 
#five, then there are 19 letters used in total. If all the numbers from 1 to 1000 (one 
#thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
#contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of 
#"and" when writing out numbers is in compliance with British usage.

sum=0
for h in range(0, 10):
    hundred=[0, 13, 13, 15, 14, 14, 13, 15, 15, 14]
    #, onehundredand, twohundredand, threehundredand, fourhundredand...
    
    for t in range(0, 10):
        tens=[0, 3, 6, 6, 6, 5, 5, 7, 6, 5] 
        #, ten, twenty, thirty, fourty, fifty, sixty, seventy, eighty, ninty
        if(t==1):
            sum=sum+hundred[h]+3 #ten
            sum=sum+hundred[h]+6 #eleven
            sum=sum+hundred[h]+6 #twelve
            sum=sum+hundred[h]+8 #thirteen
            sum=sum+hundred[h]+8 #fourteen
            sum=sum+hundred[h]+7 #fifteen
            sum=sum+hundred[h]+7 #sixteen
            sum=sum+hundred[h]+9 #seventeen
            sum=sum+hundred[h]+8 #eighteen
            sum=sum+hundred[h]+8 #nineteen
        else:
            sum=sum+hundred[h]+tens[t]
            sum=sum+hundred[h]+tens[t]+3 #one
            sum=sum+hundred[h]+tens[t]+3 #two
            sum=sum+hundred[h]+tens[t]+5 #three
            sum=sum+hundred[h]+tens[t]+4 #four
            sum=sum+hundred[h]+tens[t]+4 #five
            sum=sum+hundred[h]+tens[t]+3 #six
            sum=sum+hundred[h]+tens[t]+5 #seven
            sum=sum+hundred[h]+tens[t]+5 #eight
            sum=sum+hundred[h]+tens[t]+4 #nine
sum+=11 #onethousand
sum-=3*9 #extra "and"s
print(sum)
