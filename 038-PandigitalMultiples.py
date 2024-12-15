#Problem 38: Take the number 192 and multiply it by each of 1, 2, and 3: By concatenating each 
#product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated 
#product of 192 and (1,2,3). The same can be achieved by starting with 9 and multiplying by 1, 
#2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and 
#(1,2,3,4,5). What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
#concatenated product of an integer with (1,2,...,n) where n>1?

#I just solved it by hand
#I thought it would be easier that way and it was!
#I just needed to figure out what natural number n would be the first term
#I knew that it must be more than 918273645, 
#so the first digit of n must be 9
#and n can't be one digit long (918273645 is incorrect)
#n can't be two digits long because then 
#(1,2,3) would concatenate to an 8 digit number, 
#and (1, 2, 3, 4) would concatenate to an eleven digit number,
#and we need a nine digit number
#n can't be three digits long because then 
#(1,2) would concatenate to a seven digit number
#and (1,2,3) would concatenate to eleven digits
#Thus n must be a two digit number multiplied by (1,2)
#Now we just figure out the digits of n
#We already know the first digit of n is 9
#so then the first digits of the 2*n need to be 18
#so then the second digit of n cannot be 5 or more (because then 18->19)
#also there can't be a 4 in n, because then 2*n would have another 8
#also there can't be a 5 in n because then 2*n would have a 0 or another 1
#so I figured n's first digits had to be 93 or 92
#I realized I'd also need a 4 and 5 in the 2*n
#I tried 923_1846_ but I needed a way to get a five in 2n
#2n must be even so the five can't be the last digit of 2n
#I switched the 3 and 2 and put 7 in the last digit of n!
#and it actually came together!
#n=9327
#2*n=18654
#932718654 is pandigital!
#in code:
n=9327
n2=n*2
print(str(n)+str(n2))
