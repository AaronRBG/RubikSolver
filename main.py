import cube

c = cube.json2cube('cube3x3.json')
print(c.generateMoves())
c.printState()
c.move("L0")