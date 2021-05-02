"""
En Route Salute
===============

Commander Lambda loves efficiency and hates anything that wastes time. She's a busy lamb, after all! She generously rewards henchmen who identify sources of inefficiency and come up with ways to remove them. You've spotted one such source, and you think solving it will help you build the reputation you need to get promoted.

Every time the Commander's employees pass each other in the hall, each of them must stop and salute each other - one at a time - before resuming their path. A salute is five seconds long, so each exchange of salutes takes a full ten seconds (Commander Lambda's salute is a bit, er, involved). You think that by removing the salute requirement, you could save several collective hours of employee time per day. But first, you need to show her how bad the problem really is.

Write a program that counts how many salutes are exchanged during a typical walk along a hallway. The hall is represented by a string. For example:
"--->-><-><-->-"

Each hallway string will contain three different types of characters: '>', an employee walking to the right; '<', an employee walking to the left; and '-', an empty space. Every employee walks at the same speed either to right or to the left, according to their direction. Whenever two employees cross, each of them salutes the other. They then continue walking until they reach the end, finally leaving the hallway. In the above example, they salute 10 times.

Write a function solution(s) which takes a string representing employees walking along a hallway and returns the number of times the employees will salute. s will contain at least 1 and at most 100 characters, each one of -, >, or <.



Input:
solution.solution(">----<")


Output:
    2

    >----<
	->--<-
	--><--     |salute+=2|
	--<>--
	-<-->-
	<---->
	------

Input:
solution.solution("<<>><")
Output:
    4

    <<>><       |salut++|
    -<><>
    <-><>		|salut++|
    --<>-
    -<-->
    <----
    -----

	
	--->-><-><-->-    |salut++ salut++|
	----><>-<>--->    |salut++|
	----<>-><->---    |salut++|
	---<--><>-->--    |salut++|
	--<---<>->-->-
	-<---<-->->-->
	<--<----->->--

APPROACH:
Each Salute is 2

>< - Salute (each time count occurences of this and increment salutes)
(on advance, swap to make <>)
Like this
-><-
-<>-
<-->

> - Walking to Right
(on advance, i+1 should become > and i should become -)
if(i+1 is EOS) then disappear

< - Walking to Left
(on advance, i-1 should become < and i should become -)
if(i-1 is EOS) then disappear
"""

salutes = 0


#Correct Solution
def solution3(s):
	salut = 0
	for x in range(0, len(s)):
		if(s[x] == '>'):
			salut += 2*s[x:len(s)].count('<')
	return salut


"""
Simple Tests
<<>>< - 4
>----< - 2
--->-><-><-->- 10
"""

# s = "<>-<><->><><><><><-"
# solution(s)
# print(solution2(s))