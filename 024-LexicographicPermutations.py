#Problem 24: A permutation is an ordered arrangement of objects. For example, 3124 is one 
#possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed 
#numerically or alphabetically, we call it lexicographic order. The lexicographic 
#permutations of 0, 1 and 2 are: 012   021   102   120   201   210  What is the millionth 
#lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

""" #First attempt
def mutat(array, level):
    copy=[]
    for a in array:
        copy.append(a)
    temp=copy[-level]
    copy[-level]=copy[-level-1]
    copy[-level-1]=temp
    return copy

muta=[]
example=[0,1,2,3]
muta.append(example)
muta.append(mutat(example, 1))
muta.append(mutat(example, 2))
muta.append(mutat(mutat(example, 2),1))
muta.append(mutat(mutat(example, 1),2))
muta.append(mutat(mutat(mutat(example, 1),2),1))
muta.append(mutat(example, 3))
muta.append(mutat(mutat(example, 3),1))
muta.append(mutat(mutat(example, 3),2))
muta.append(mutat(mutat(mutat(example, 3),2),1))
muta.append(mutat(mutat(mutat(example, 3),1),2))
muta.append(mutat(mutat(mutat(mutat(example, 3),1),2),1))
muta.append(mutat(mutat(example, 2),3))
muta.append(mutat(mutat(mutat(example, 2),3),1))
muta.append(mutat(mutat(mutat(example, 2),3),2))
muta.append(mutat(mutat(mutat(mutat(example, 2), 3),2),1))
muta.append(mutat(mutat(mutat(mutat(example, 2),3),1),2))
muta.append(mutat(mutat(mutat(mutat(mutat(example, 2),3),1),2),1))
muta.append(mutat(mutat(mutat(example, 1),2),3))
muta.append(mutat(mutat(mutat(mutat(example, 1),2),3),1))
muta.append(mutat(mutat(mutat(mutat(example, 1),2),3),2))
muta.append(mutat(mutat(mutat(mutat(mutat(example, 1),2),3),2),1))
muta.append(mutat(mutat(mutat(mutat(mutat(example, 1),2),3),1),2))
muta.append(mutat(mutat(mutat(mutat(mutat(mutat(example, 1),2),3),1),2),1))

print(muta)"""


permutations=[]

#this function outputs a mutation of the list "array" by swapping two items
#m stands for mutate
def m(array, index):
    if len(array)>index:
        copy=[]
        for a in array:
            copy.append(a)
        temp=copy[-index]
        copy[-index]=copy[-index-1]
        copy[-index-1]=temp
        return copy

#this function calls m() recursively
#c stands for call
#lev stands for level
def c(array, level):
    if level==1:
        permutations.append(array)
    else:
        #here the for loop interates backwards 
        #line 71 calls on level, level-1, level-2...until 1
        for i in range(0, level):
            copy=[]
            for a in array:
                copy.append(a)
                
            while i>0:
                copy=m(copy, level-i)
                i=i-1
            c(copy, level-1)
        
    
length=int(input("How long do you want the list?"))
if(length>8):
    print("This may a take a while")
list=[]
for i in range(0, length):
    list.append(i)
c(list, length)
yes=input("Do you want to see a particular permutation?")
if yes=="yes":
    index=int(input("What index?"))
    print(permutations[index-1])
yes=input("Do you want the length of the list?")
if yes=="yes":
    print(len(permutations))
yes=input("Do you want to see the list of permutations?")
if yes=="yes":
    for i in range(0, len(permutations)):
        print(i+1, permutations[i])
