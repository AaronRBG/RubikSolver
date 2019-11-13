#!/usr/bin/python
from problem import Problem
from search_algorithm import limited_search, search

filename_output = "solution.txt"

def writeFile(filename, text):
    with open(filename, 'a') as outfile:
        outfile.write(text+"\n")

print('--------- Introduce the type of algortihm ---------')
print('--------- Options: BFS, DFS, UCS, LDS, IDS, Greedy, A* ---------')
algorithm = str(input())
print('--------- Introduce the json filename of the Initial_state: ---------')
filename_input = str(input())
print('--------- Introduce the maximum depth of the nodes of the problem: ---------')
depth = int(input())
if algorithm == "IDS":
	print('--------- Introduce the incremental constant of the depth (if it is necessary for IDS): ---------')
	inc_depth = int(input())
else:
	inc_depth = 0
Prob = Problem(filename_input) #Clase Problem with InitialState and functions isGoal and sucessors
sol = search(Prob, algorithm, depth, inc_depth)
if sol is not None:
	print('############### The SOLUTION of the cube with movements is the next one: #################')
	for i in range(len(sol)-1,0,-1):
	    print(sol[i-1].action)
	    writeFile(filename_output, sol[i-1].action)
	    writeFile(filename_output, str(sol[i-1].state.faces))
else:
	print('############### No solution was found #################')