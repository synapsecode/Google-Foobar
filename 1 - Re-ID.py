"""
=================================================
Re-ID
=================================================
Next time Bunny HQ needs someone to infiltrate a space station to rescue prisoners, you're going to tell them to make sure 'stay up for 48 hours straight scrubbing toilets' is part of the job description. It's only fair to warn people, after all.

There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other 
"good" numbers have been lording it over the poor minions who are stuck with more boring IDs. To quell the unrest, 
Commander Lambda has tasked you with reassigning everyone new, random IDs based on her Completely Foolproof Scheme. 

She's concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion must draw a 
number from a hat. That number is the starting index in that string of primes, and the minion's new ID number will be the next 
five digits in the string. So if a minion draws "3", their ID number will be "71113". 

Help the Commander assign these IDs by writing a function solution(n) which takes in the starting index n of Lambda's string 
of all primes, and returns the next five digits in the string. Commander Lambda has a lot of minions, so the value of n will 
always be between 0 and 10000.

"""
def solution(n):
	#IsPrime Method (O(sqrtN))
	def is_prime(n):
		ret = False
		i = 2
		if(n<2): return False
		while(i*i <= n):
			if(n%i==0):
				return False
			i+=1
		return True

	#Generate Prime string
	s = ""
	i = 2
	while(len(s) < n + 5):
		if(is_prime(i)):
			s+=str(i)
		i+=1
	# return s[n:n+5]
	print(s[n:n+5])

n = int(input("Enter Number: "))
solution(n)