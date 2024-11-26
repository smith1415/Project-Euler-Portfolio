#Problem 15: Starting in the top left corner of a 2 x 2 grid, and only being able to move 
#to the right and down, there are exactly 6 routes to the bottom right corner. How many 
#such routes are there through a 20 x 20 grid?

#attempt 1
"""def paths(x, y):
    if x==0:
        return 1
    elif y==0:
        return 1
    else:
        return paths(x,y-1)+paths(x-1, y)
numX=int(input("What is the rectangle width?"))
numY=int(input("What is the rectangle height?"))
print("paths:", paths(numX, numY))"""

#attempt 2 (for efficiency)
def paths(x, y):
    if x==0:
        return 1
    elif y==0:
        return 1
    else:
        if rowcol[x-1][y-1]==0:
            value=paths(x,y-1)+paths(x-1, y)
            rowcol[x-1][y-1]=value
            rowcol[y-1][x-1]=value
            return value
        else:
            return rowcol[x-1][y-1]

numX=int(input("What is the rectangle width?"))
numY=int(input("What is the rectangle height?"))

rowcol=[]
for i in range(0, numX):
    row=[]
    for j in range(0, numY):
        row.append(0)
    rowcol.append(row)

print("paths:", paths(numX, numY))
