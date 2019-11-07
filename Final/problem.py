from cube import Cube
from node import Node
from frontier import Frontier
import random

class Problem:

	def __init__(self):  # constructor

		print('Introduce the json filename of the Initial_state')
		filename = input()

		self.Initial_state = Cube()
		self.Initial_state.json2cube(filename)
		self.createGoal()

	def createGoal(self):

		goal_cube = Cube()
		length=0
		string = ""

		for state in self.Initial_state.faces.values():
			for i in state:
				for j in i:
					length+=1
			break

		color2position = {0: 3, 1: 1, 2: 2, 3: 4, 4: 5, 5: 0}

		for i in range(6):
			for j in range(int(length)):
				string+=str(color2position[i])
		goal_cube.cubeMD5(string)

		self.goal = goal_cube.id

	def isGoal(self,state):

		if state.id == self.goal:
			return True
		return False

	def sucessors(state):

		ret = [ Cube() for i in range(12)]

		state.cube2Json("saved/"+"state.json")

		for i in range(12):
			ret[i].json2cube("saved/"+"state.json")

		moves = iter(state.generateMoves())

		for i in range(12):

			movement = next(moves)
			ret[i].move(movement)
			ret[i] = (movement,ret[i],1)

		return ret

p = Problem()
print(p.isGoal(p.Initial_state))
