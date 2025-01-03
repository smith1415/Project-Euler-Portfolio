#Problem 96: Su Doku (Japanese meaning number place) is the name given to a popular puzzle 
#concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a 
#similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku 
#puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, 
#column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical 
#starting puzzle grid and its solution grid.
"""
<p096_1.png>     <p096_2.png>
"""
#A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although 
#it may be necessary to employ "guess and test" methods in order to eliminate options (there is 
#much contested opinion over this). The complexity of the search determines the difficulty of 
#the puzzle; the example above is considered easy because it can be solved by straight forward 
#direct deduction. The 6K text file, sudoku.txt (hyperlink to 
#https://projecteuler.net/project/resources/p096_sudoku.txt) (right click and 'Save Link/Target 
#As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique 
#solutions (the first puzzle in the file is the example above). By solving all fifty puzzles 
#find the sum of the 3-digit numbers found in the top left corner of each solution grid; for 
#example, 483 is the 3-digit number found in the top left corner of the solution grid above.

#https://docs.google.com/document/d/159d0Gc1aZUu0RP0ql4_7iA6eHB33Gw37WxZxUWfvV20/edit?tab=t.0
#reformatted the file into something more legible
#used find and replace to have 0->_
#and I made the font size bigger
#now I'm solving them by hand. I enjoy doing sudoku :)

#here are top left corner values that I've found so far:
#(I just put 0s if I haven't found it yet)

list=[483, 245, 462, 137, 523, 100,
     43, 487, 0, 1, 0, 962,
     300, 630, 0, 361, 50, 80,
     3, 0, 20, 5, 40, 4,
     360, 500, 7, 0, 30, 200,
     0, 0, 608, 50, 53, 6,
     5, 0, 0, 0, 0, 380,
     0, 10, 80, 904, 0, 1,
     0, 302]

print(sum(list))
print(list)
