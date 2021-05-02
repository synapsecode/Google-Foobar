"""
Doomsday Fuel
=============

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel. 

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly. 

For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].


[0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
[4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
[0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
[0,0,0,0,0,0],  # s3 is terminal
[0,0,0,0,0,0],  # s4 is terminal
[0,0,0,0,0,0]


(MARKOV ABSORBING CHAIN) - https://www.youtube.com/watch?v=bTeKu7WdbT8 (EP7&9)

"""
import pprint

"""
orig: https://github.com/Trismeg/FooBar/blob/master/doomsday_fuel.py
DEF SOLUTION
1. Mutate Matrix to add a diagonal of Zeros Initially
2. Store the Sum of each row in a list (row_summations)
3. Get the Index of all Zeros in row_summations and store it in a list (We get indexes of Terminal States)
4. Similarly, the rows where sum isnt zero contain non-terminal states
5. MainLoop
		(YET TO FIGURE OUT)
6. Ways to reach terminal states are in the first row of matrix
7. Sum matrix[0] to get common denominator and append it to output
8. Handle Zero Denominator Cases
9. Return Output
"""

#Takes a list and returns the GCD
def sequential_gcd(R):
	
	#GCD Function
	gcd = lambda a, b: a if (b == 0) else gcd(b, a%b)

	L = len(R)
	final_gcd = 0
	for n in R:
		final_gcd = gcd(final_gcd, n)
	return final_gcd


def fuse(a, ida, b, idb):
	lenA = len(a)
	indices = set(range(lenA)) - {ida, idb} #All Indexes upto a, except id of a & b
	sum_B = sum(b)
	out = [0 for _ in a] #Zero List of length a

	for i in indices:
		#out will have length of len(indices)
		#puts (sum of b * value of a at i) + (value of a at index of b * value of b at i)
		out[i] = (sum_B * a[i]) + (a[idb] * b[i])

	gcd = sequential_gcd(out) #Gets the SEQ_GCD of the out array

	#Simplification
	output = [e//gcd for e in out] #IntegerDivide every element with its SEQ_GCD

	return output


def solution(M):
	height = len(M); width = len(M[0])
	matrix = list(M)

	#Mutate matrix to add Diagonal of Zeros
	for i, e in enumerate(matrix):
		e[i] = 0

	#Sum of each row in Matrix
	row_summations = [sum(i) for i in matrix]

	#(Terminal State Row Indexes)
	terms = [i for i,e in enumerate(row_summations) if e==0]
	#(Non Terminal State Row Indexes)
	non_terms = [i for i,e in enumerate(row_summations) if e!=0]

	L = len(non_terms) #Length of 

	#Mainloop Runs On and Upto Non-Terminal State Rows
	for i in range(0, L-1):
		index_B = non_terms[L-i-1]
		for j in range(0, L-1):
			index_A = non_terms[j]
			matrix[index_A] = fuse(matrix[index_A], index_A, matrix[index_B], index_B)


	#The first row of the matrix contains all the ways to reach terminal state
	#for each state encoded in its index
	output = [matrix[0][i] for i in terms]


	denominator = sum(output)
	output.append(denominator) #Add the Denominator to end of list as required

	#Case to Handle if the Denominator is Zero, We just append 1s and take len as denominator
	if(denominator == 0):
		output = [1 for _ in terms]
		output.append(len(terms))

	return output


mat=[
  [1,1,1,3,4,1,1,2],  
  [4,1,3,3,2,3,0,4], 
  [0,0,0,1,0,0,8,9], 
  [0,0,3,0,0,0,0,0],
  [0,0,0,0,0,0,0,0], #terminal
  [0,0,0,0,0,0,0,0],  # terminal
  [0,0,0,0,0,0,0,0],  # terminal
  [0,0,0,0,0,0,0,0],  # terminal
]

M = [
	[0,1,0,0,0,1],
	[4,0,0,3,2,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0]
]

M2 = [
	[0, 2, 1, 0, 0],
	[0, 0, 0, 3, 4], 
	[0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0]
]



print(solution(mat))
print(solution(M))
print(solution(M2))