class Frontier:

    def __init__(self):
        self.frontier = []

    def insertNode(self, treeNode): #Insert a node in the correct position, maintaining the ascending order
                                    #of f value
        if len(self.frontier) == 0:
            self.frontier.append(treeNode)
        else:
            count = len(self.frontier) - 1
            while count >= 0:
                if self.frontier[count].f <= treeNode.f:
                    self.frontier.insert(count + 1, treeNode)
                    break
                count -= 1
            if count < 0:
                self.frontier.insert(0, treeNode)

    def removeNode(self): #Remove first node from the frontier
        if self.frontier:
            treeNode = self.frontier.pop(0)
            return treeNode
        else:
            return None

    def isEmpty(self):
        if not self.frontier:
            return True
        else:
            return False

    def insertList(self, listNodes): #Insert a node in the correct position, maintaining the ascending order
        if listNodes is not None:                            #of f value
            for node in listNodes:
                self.insertNode(node)
