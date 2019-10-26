import cube

def successors(stateJSON):

	ret = []

	cube = Cube()
	cube.json2cube(stateJSON)
	
	moves = iter(state.generateMoves())

	for i in range(12):

		movement = next(moves)
		new_cube = cube
		new_cube.move(movement)
		succesor = (movement, new_cube, 1)
		print(successor)
		ret.append(succesor)

	return ret

print('Introduce a json filename')
filename = input()
sucessors(filename)
