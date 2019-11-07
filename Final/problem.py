from cube import Cube
from node import Node
from frontier import Frontier
import random
import numpy as np
import copy

class Problem:

	def __init__(self, Initial_state):  # constructor
		initial_cube = Cube()
		goal_cube = Cube()

		initial_cube.json2cube(Initial_state)

		length=0
		for state in initial_cube.faces.values():
			for i in state:
				for j in i:
					length+=1
			break

		string = ""
		color2position = {0: 3, 1: 1, 2: 2, 3: 4, 4: 5, 5: 0}
		for i in range(6):
			for j in range(int(length)):
				string+=str(color2position[i])
		goal_cube.cubeMD5(string)

		self.Initial_state = initial_cube
		self.goal = goal_cube.id

	def isGoal(self,state):
		state.cubeMD5()
		if state.id == self.goal:
			return True
		return False

	def successors(self, state):
		#suc = [Cube() for i in range(12)]
		ret = []
		#initial_faces = state.faces
		#for i in range(12):
		#	suc[i].faces = initial_faces
		
		moves = iter(state.generateMoves())
		for i in range(12):
			movement = next(moves)
			new_suc = copy.deepcopy(state)
			new_suc.move(movement)
			succesor = (movement, new_suc, 1)
			ret.append(succesor)
		return ret
