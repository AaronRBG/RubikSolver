from cube import Cube

def successors(stateJSON):

	ret = []

	cube = Cube()
	cube.json2cube(stateJSON)
	
	moves = iter(cube.generateMoves())

	for i in range(12):

		movement = next(moves)
		new_cube = cube
		new_cube.move(movement)
		successor = (movement, new_cube, 1)
		ret.append(successor)

	return ret

print('Introduce a json filename')
filename = input()
print(successors(filename))
