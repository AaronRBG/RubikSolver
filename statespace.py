from treenode import Treenode
from cube import Cube
import random

def sucessors(node):

	state = node.state
	c = Cube(None,None)

	ret = [ None for i in range(12)]

	state.cube2Json("state.json")
	c.json2cube("state.json")

	for i in range(12):
		ret[i] = Treenode(1,c,node.cost+1,"",node.d+1,random.randint(1,101),c)

	moves = iter(state.generateMoves())

	for i in range(12):

		movement = next(moves)
		ret[i].state.move(movement)

	return ret

print('Introduce a json filename')
filename = input()
c = Cube(None,None)
c.json2cube(filename)
t = Treenode(1, c, 1, "", 1, random.randint(1,101), parent=None)
print(sucessors(t))