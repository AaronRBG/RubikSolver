
class Frontier:

    def __init__(self):
        self.frontier = []

    def insert(self, treeNode):
        if len(self.frontier) == 0:
            self.frontier.append(treeNode)
        else:
            count = len(self.frontier) - 1
            while count >= 0:
                if self.frontier[count].f < treeNode.f:
                    self.frontier.insert(count+1, treeNode)
                    break
                elif self.frontier[count].f == treeNode.f:
                    if self.frontier[count].id < treeNode.id:
                        self.frontier.insert(count+1, treeNode)
                        break
                count -= 1
            if count < 0:
                self.frontier.insert(0, treeNode)
                 
    def remove(self):
        treeNode = self.frontier.pop(0)
        return treeNode

    def isEmpty(self):
        if not self.frontier:
            return True
        else:
            return False
