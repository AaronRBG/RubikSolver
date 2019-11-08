from cube import Cube

def sucessors(state):

	moves = iter(state.generateMoves())

	ret = [ Cube() for i in range(len(moves))]

	state.cube2Json("saved/"+"state.json")

	for i in range(len(moves)):
		ret[i].json2cube("saved/"+"state.json")

	for i in range(len(moves)):

		movement = next(moves)
		ret[i].move(movement)
		ret[i] = (movement,ret[i],1)

	return ret

print('Introduce a json filename')
filename = input()
c = Cube()
c.json2cube(filename)
print(sucessors(c))