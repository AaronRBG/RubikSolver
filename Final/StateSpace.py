from cube import Cube

def sucessors(state):

	ret = [ Cube(None,None) for i in range(12)]

	state.cube2Json("state.json")

	for i in range(12):
		ret[i].json2cube("state.json")

	moves = iter(state.generateMoves())

	for i in range(12):

		movement = next(moves)

		ret[i].move(movement)
		print(movement,ret[i],1)

	return ret

print('Introduce a json filename')
filename = input()
c = Cube(None,None)
c.json2cube(filename)
print(sucessors(c))
