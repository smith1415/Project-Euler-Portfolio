#Problem 19: You are given the following information, but you may prefer to do some #research for yourself.
#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is
#divisible by 400.

#How many Sundays fell on the first of the month during the twentieth century (1 Jan 
#1901 to 31 Dec 2000)?

#counting each day since Jan 1 1900, which was a monday, means that
#Sundays fall on days where day%7==0
day=1 
month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#got to fast forward one year because the 19th century started in 1901
#keep in mind that 1900 was NOT a leap year
for m in month:
    day+=m
#Now, we are at Jan. 1st, 1901, and we need to go to Dec. 31st 2000
count=0
for i in range (1, 101):
    for j in range (0, 12):
        if day%7==0:
            count=count+1
        if j==1 and i%4==0:
            day=day+month[j]+1 #leap years
        else:
            day=day+month[j]
        
print(count)
