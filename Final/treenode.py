class Treenode:
	
    def __init__(self, state, cost, action, d, f, parent=None):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.action = action
        self.d = d
        self.f = f       
