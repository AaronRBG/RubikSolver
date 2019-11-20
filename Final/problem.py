from cube import Cube
from node import Node
from frontier import Frontier
from statespace import successorsCube
import random

class Problem:

	def __init__(self,Initial_state_json):  # constructor

		self.createInitialCube(Initial_state_json)

	def createInitialCube(self, Initial_state):
		c = Cube()
		c.json2cube(Initial_state)
		self.Initial_state = c

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