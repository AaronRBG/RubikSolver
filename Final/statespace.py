from cube import Cube
import copy

def successorsCube(state):

	moves = iter(state.generateMoves())

	ret = [ Cube() for i in range(len(state.generateMoves()))]

	for i in range(len(state.generateMoves())):
		
		ret[i] = copy.deepcopy(state)
		movement = next(moves)
		ret[i].move(movement)
		ret[i] = (movement,ret[i],1)

	return ret