#Problem 64: All square roots are periodic when written as continued fractions and can be written in 
#the form: sqrt(N)=a<0>+1/(a<1>+1/(a<2>+1/(a<3>+...))). It can be seen that the sequence is 
#repeating. For conciseness, we use the notation sqrt(23)=[4;(1,3,1,8)], to indicate that the block 
#(1,3,1,8) repeats indefinitely. The first ten continued fraction representations of (irrational) 
#square roots are: 
"""
sqrt(2)=[1;(2)], period=1
sqrt(3)=[1;(1,2)], period=2
sqrt(5)=[2;(4)], period=1
sqrt(6)=[2;(2,4)], period=2
sqrt(7)=[2;(1,1,1,4)], period=4
sqrt(8)=[2;(1,4)], period=2
sqrt(10)=[3;(6)], period=1
sqrt(11)=[3;(3,6)], period=2
sqrt(12)=[3;(2,6)], period=2
sqrt(13)=[3;(1,1,1,1,6)], period=5
"""
#Exactly four continued fractions, for N<=13, have an odd period. How many continued fractions for 
#N<=10000 have an odd period?
