class Node:
    id = 0
	
    def __init__(self, state=None, cost=0, action="", d=0, f=0,h=-5, parent=None):
	self.id += 1
        self.state = state
        self.parent = parent
        self.cost = cost
        self.action = action
        self.d = d
        self.f = f
        self.h = h
