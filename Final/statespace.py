from cube import Cube

def sucessors(state):

	ret = [ Cube() for i in range(12)]

	state.cube2Json("saved/"+"state.json")

	for i in range(12):
		ret[i].json2cube("saved/"+"state.json")

	moves = iter(state.generateMoves())

	for i in range(12):

		movement = next(moves)
		ret[i].move(movement)

	return ret

print('Introduce a json filename')
filename = input()
c = Cube()
c.json2cube(filename)
print(sucessors(c))