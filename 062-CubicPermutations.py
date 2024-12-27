#Problem 62: The cube, 41063625 (345**3), can be permuted to produce two other cubes: 56623104 
#(384**3) and 66430125 (405**3). In fact, 41063625 is the smallest cube which has exactly three 
#permutations of its digits which are also cube. Find the smallest cube for which exactly five 
#permutations of its digits are cube.

def cube(num):
    return num**3

def place(num):
    for i in range(0, len(cd)):
        if len(order)<=len(cd[i][0]) and int(order)<int(cd[i][0]):
            return i
    return -1
i=2
#cd=cube digits
cd=[['1',1], ['8', 8]]
notFound=True
while notFound:
    i+=1
    cubeVal=cube(i)
    c=cubeVal
    digits=[]
    while c > 0:
        digits.append(c%10)
        c=int(c/10)
    digits.sort()
    order=""
    for d in digits:
        order=order+str(d)
    p=place(order)
    if p==-1:
        cd.append([order, cubeVal])
    else:
        cd.insert(p, [order, cubeVal])
    if cd[p][0]==cd[p-1][0]:
        print("FOUND pair", cd[p-1][1], cd[p][1])
        if cd[p][0]==cd[p-2][0]:
            print("FOUND triple", cd[p-2][1], cd[p-1][1], cd[p][1])
            if cd[p][0]==cd[p-3][0]:
                print("FOUND quad", cd[p-3][1], cd[p-2][1], cd[p-1][1], cd[p][1])
                if cd[p][0]==cd[p-4][0]:
                    print("FOUND quint", cd[p-4][1], cd[p-3][1], cd[p-2][1], cd[p-1][1], cd[p][1])
                    notFound=False
                    print(cd)
