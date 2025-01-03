#Problem 68: Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each 
#line adding to nine.
"""
<picture of "magic" 3-gon ring>
"""
#Working clockwise, and starting from the group of three with the numerically lowest external 
#node (4,3,2 in this example), each solution can be described uniquely. For example, the above 
#solution can be described by the set: 4,3,2; 6,2,1; 5,1,3. It is possible to complete the ring 
#with four different totals: 9, 10, 11, and 12. There are eight solutions in total.
"""
Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6
"""
#By concatenating each group it is possible to form 9-digit strings; the maximum string for a 
#3-gon ring is 432621513.Using the numbers 1 to 10, and depending on arrangements, it is possible 
#to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?
"""
<picture of empty "magic" 5-gon ring>
"""

#solved by hand lol
#Since the string starts with the smallest external node, 
#first priority is making the smallest external node as large as possible
#Thus 10,9,8,7,6 are the external nodes and 5,4,3,2,1 are the internal nodes 
#(and therefore counted twice in the total sum of legs)
#The total sum is 10+9+8+7+6+2(5+4+3+2+1)=40+2(15)=70
#70/5=14, each group must have a sum of 14
#9 and 10 should probably share the 1 and then the rest fall into place:
#9-1-4=14
#10-3-1=14
#6-5-3=14
#7-2-5=14
#8-4-2=14
#each group equals 14!
#concatenate clockwisely starting with 6-5-3
output="653"
output+="1031"
output+="914"
output+="842"
output+="725"
print(output)
