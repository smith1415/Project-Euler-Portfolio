#Problem 5: 2520 is the smallest number that can be divided by each of the numbers from 
#1 to 10 without any remainder. What is the smallest positive number that is evenly 
#divisible by all of the numbers from 1 to 20?

def findLowestMultiples(num, start, end, array):
    for i  in range(start, end):
        if num%i==0:
            array.append(i)
            return findLowestMultiples(int(num/i), i, int(num/i)+1, array)
    return array

list=[]
for i in range(2, 21):
    factors=findLowestMultiples(i, 2, i+1, [])
    currentlist=[]
    for already in list:
        currentlist.append(already)
    for f in factors:
        if f in currentlist:
            currentlist.remove(f)
        else:
            list.append(f)
    print(list)
output=1
for i in list:
    output=output*i

print(output)
