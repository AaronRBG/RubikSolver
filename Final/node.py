class Node:
    id = 0
    
    def __init__(self, id=0, state=None, cost=0, action="", d=0, f=None,h=None, parent=None):
        self.id = id
        self.state = state
        self.parent = parent
        self.cost = cost
        self.action = action
        self.d = d
        self.f = f
        self.h = h