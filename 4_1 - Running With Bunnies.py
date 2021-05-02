"""
Running with Bunnies
====================

You and your rescued bunny prisoners need to get out of this collapsing death trap of a space station - and fast! Unfortunately, some of the bunnies have been weakened by their long imprisonment and can't run very fast. Their friends are trying to help them, but this escape would go a lot faster if you also pitched in. The defensive bulkhead doors have begun to close, and if you don't make it through in time, you'll be trapped! You need to grab as many bunnies as you can and get through the bulkheads before they close. 

The time it takes to move from your starting point to all of the bunnies and to the bulkhead will be given to you in a square matrix of integers. Each row will tell you the time it takes to get to the start, first bunny, second bunny, ..., last bunny, and the bulkhead in that order. The order of the rows follows the same pattern (start, each bunny, bulkhead). The bunnies can jump into your arms, so picking them up is instantaneous, and arriving at the bulkhead at the same time as it seals still allows for a successful, if dramatic, escape. (Don't worry, any bunnies you don't pick up will be able to escape with you since they no longer have to carry the ones you did pick up.) You can revisit different spots if you wish, and moving to the bulkhead doesn't mean you have to immediately leave - you can move to and from the bulkhead to pick up additional bunnies if time permits.

In addition to spending time traveling between bunnies, some paths interact with the space station's security checkpoints and add time back to the clock. Adding time to the clock will delay the closing of the bulkhead doors, and if the time goes back up to 0 or a positive number after the doors have already closed, it triggers the bulkhead to reopen. Therefore, it might be possible to walk in a circle and keep gaining time: that is, each time a path is traversed, the same amount of time is used or added.

Write a function of the form solution(times, time_limit) to calculate the most bunnies you can pick up and which bunnies they are, while still escaping through the bulkhead before the doors close for good. If there are multiple sets of bunnies of the same size, return the set of bunnies with the lowest prisoner IDs (as indexes) in sorted order. The bunnies are represented as a sorted list by prisoner ID, with the first bunny being 0. There are at most 5 bunnies, and time_limit is a non-negative integer that is at most 999.

For instance, in the case of
[
  [0, 2, 2, 2, -1],  # 0 = Start
  [9, 0, 2, 2, -1],  # 1 = Bunny 0
  [9, 3, 0, 2, -1],  # 2 = Bunny 1
  [9, 3, 2, 0, -1],  # 3 = Bunny 2
  [9, 3, 2, 2,  0],  # 4 = Bulkhead
]
and a time limit of 1, the five inner array rows designate the starting point, bunny 0, bunny 1, bunny 2, and the bulkhead door exit respectively. You could take the path:

Start End Delta Time Status
    -   0     -    1 Bulkhead initially open
    0   4    -1    2
    4   2     2    0
    2   4    -1    1
    4   3     2   -1 Bulkhead closes
    3   4    -1    0 Bulkhead reopens; you and the bunnies exit

With this solution, you would pick up bunnies 1 and 2. This is the best combination for this space station hallway, so the answer is [1, 2].

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([
		[0, 2, 2, 2, -1],  #0   start
		[9, 0, 2, 2, -1],  #1   Bunny0
		[9, 3, 0, 2, -1],  #2	Bunny1
		[9, 3, 2, 0, -1],  #3	Bunny2
		[9, 3, 2, 2, 0]    #4	bulkhead
	], 1)

	We generally move to the next bunny, Unless there exists a pathway which can yeild us more time(negative cell value) We go to that path and then come back to next bunny and try again.

	But if none are -1, then we may go to next bunny but if we find that another path to a bunny is shorter, we take that (if many exists, take the left most (first))



	Start End Delta Time Status
	-      0    -    1      [OPEN]
	0      4    -1   2      [OPEN]   > We went to 4 because it had -1
	4      2    2    0      [OPEN]   > Picked Bunny1



Output:
    [1, 2]

Input:
solution.solution([
		[0, 1, 1, 1, 1], #0 start
		[1, 0, 1, 1, 1], #1      Bunny0
		[1, 1, 0, 1, 1], #2		 Bunny1
		[1, 1, 1, 0, 1], #3		 Bunny2
		[1, 1, 1, 1, 0]	 #4 bulkhead
	], 3)


	Start End Delta Time Status
	-     0    -     3   	[OPEN]
	0     1    1     2      [OPEN]  > Pick Bunny0
	1     4    1     1      [OPEN]  > Bunny0 has escaped
	4     2    1     0      [OPEN]  > Pick Bunny1
	2     4    1     -1     [JUST CLOSED] > Bunny1 has escaped

	Start End Delta Time Status
	-     0    -     3   [OPEN]
	0     1    1     2   [OPEN]  > b0
	1     2    1     1   [OPEN]  > b0, b1
	2     3    1     0   [OPEN]  > b0, b1, b2
	3     4    1    -1   [JUST CLOSED] > 

	Here, we could drop at -1 because we can do a dramatic exit
	how do we stop? We check in that row if theres a -1, if yes go to that
	so that your time increases. Else youre done


Output:
    [0, 1]


Clues: Edmonds' blossom-contraction algorithm for maximum carnality matching in general graphs
Traveling Salesman Problem.???



SOL:https://github.com/DevAlone/google_foobar_solutions/blob/master/level%204/Free%20the%20Bunny%20Prisoners/main.py


Constraints:
1. At Max 5 Bunnies
	=> 7 Rows (5Bunnies + 1Start + 1End)
		=> 7 columns (Time required to go to each row from that row)



BELLMAN FORD????
FLOYD-WARSSHALL ALGORITHM
Edmonds' blossom-contraction algorithm for maximum carnality matching in general graphs

"""
import itertools

def convert_to_path(perm):
    perm = list(perm)
    perm = [0] + perm + [-1]
    path = list()
    for i in range(1, len(perm)):
        path.append((perm[i - 1], perm[i]))
    return path

def answer(time, time_limit):
    rows = len(time)
    bunnies = rows - 2

    for k in range(rows):
        for i in range(rows):
            for j in range(rows):
                if time[i][j] > time[i][k] + time[k][j]:
                    time[i][j] = time[i][k] + time[k][j]

    for r in range(rows):
        if time[r][r] < 0:
            return [i for i in range(bunnies)]

    for i in reversed(range(bunnies + 1)):
        for perm in itertools.permutations(range(1, bunnies + 1), i):
            total_time = 0
            path = convert_to_path(perm)
            print(path)
            for start, end in path:
                total_time += time[start][end]
            if total_time <= time_limit:
                return sorted(list( i - 1 for i in perm ))
    return None



L = [
  [0, 2, 2, 2, -1],  # 0 = Start
  [9, 0, 2, 2, -1],  # 1 = Bunny 0
  [9, 3, 0, 2, -1],  # 2 = Bunny 1
  [9, 3, 2, 0, -1],  # 3 = Bunny 2
  [9, 3, 2, 2,  0],  # 4 = Bulkhead
]
print(answer(L, 1))