#!/usr/bin/python
from problem import Problem
from search_algorithm import limited_search, search

filename_output = "solution.out"

def writeFile(filename, text):
    with open(filename, 'a') as outfile:
        outfile.write(text+"\n")

print('--------- Introduce the type of algortihm: ---------')
algortihm = str(input())
print('--------- Introduce the json filename of the Initial_state: ---------')
filename_input = str(input())
print('--------- Introduce the maximum depth of the nodes of the problem: ---------')
depth = int(input())
print('--------- Introduce the incremental constant of the depth (if it is necessary for IDS): ---------')
inc_depth = int(input())
Prob = Problem(filename) #Clase Problem with InitialState and functions isGoal and sucessors
sol = search(Prob, algortihm, depth, inc_depth)
print('############### The SOLUTION of the cube with movements is the next one: #################')
for i in range(len(sol)-1,0,-1):
    print(sol[i-1].action)
    writeFile(filename_output, sol[i-1].action)
    writeFile(filename_output, str(sol[i-1].state))

