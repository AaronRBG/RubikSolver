from cube import Cube

c = Cube(None,None)
c.json2cube('cubeExample.json')
c.printState()
c.move("l0")
c.printState()