from cube import Cube
from node import Node
from frontier import Frontier
from statespace import successorsCube
import random

class Problem:

	def __init__(self,Initial_state_json):  # constructor

		self.createInitialCube(Initial_state_json)
		#self.createGoal()
	def createInitialCube(self, Initial_state):
		c = Cube()
		c.json2cube(Initial_state)
		self.Initial_state = c

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

		x=0

		for face in state.faces.values():
			for i in range(len(face)):
				for j in range(len(face[i])):
					if i==0 and j==0:
						x=face[i][j]
					else:
						if not face[i][j] == x:
							return False
		return True

	def successors(self,state):
		return successorsCube(state)