class Node:
	
    def __init__(self, id=0, state=None, cost=0, action="", d=0, f=0, parent=None):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.action = action
        self.d = d
        self.f = f       