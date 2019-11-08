from cube import Cube

def successorsCube(state):

	moves = iter(state.generateMoves())

	ret = [ Cube() for i in range(len(state.generateMoves()))]

	state.cube2Json("saved/"+"state.json")

	for i in range(len(state.generateMoves())):
		ret[i].json2cube("saved/"+"state.json")

	for i in range(len(state.generateMoves())):

		movement = next(moves)
		ret[i].move(movement)
		ret[i] = (movement,ret[i],1)

	return ret
