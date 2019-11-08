from frontier import Frontier
from problem import Problem
from node import Node
from cube import Cube
import json
import time

def limited_search(Prob, strategy, max_depth):
    fringe = Frontier()
    initial_node = Node(0,Prob.Initial_state, 0, 0, 0)
    fringe.insertNode(initial_node)
    closed = []
    solution = False
    optimization = False
    cut = False
    while (solution is not True) and (fringe.isEmpty() is not True):
        current_node = fringe.removeNode()
        if Prob.isGoal(current_node.state):
            solution = True
        else:
            if nodeVisited(current_node, closed, optimization):
                cut = True
            else:
                cut = False
            if not cut:
                ls = Prob.successors(current_node.state)
                ln = createListNodes(ls, current_node, max_depth, strategy) #Do createListNodes function
                fringe.insertList(ln)
                closed.append(current_node)
                print(str(len(fringe.frontier))+" "+str(len(closed)))
            else:
                print("CUT")
    if solution:
        return createSolution(current_node) #Do createSolution function
    else:
        return None

def search(Prob, strategy, max_depth, inc_depth):
    current_depth = inc_depth
    solution = None
    while (not solution) and (current_depth <= max_depth):
        solution = limited_search(Prob, strategy, current_depth)
        current_depth += inc_depth
    return solution

def createListNodes(ls, current_node, max_depth, strategy):
    cost_current = current_node.cost
    d_current = current_node.d
    f_current = current_node.f
    ln = [Node() for i in range(len(ls))]

    if d_current == max_depth:
        print(0)
        return None

    for i in range(len(ls)):
        ln[i].action = ls[i][0]
        ln[i].state = ls[i][1]
        ln[i].cost = ls[i][2] + cost_current
        ln[i].parent = current_node
        ln[i].d = d_current + 1
        if strategy == 'DFS':
            ln[i].f = 1 / (ln[i].d + 1)

        elif strategy == 'BFS':
            ln[i].f = ln[i].d

        elif strategy == 'UCS':
            ln[i].f = ln[i].cost

        elif strategy == 'LDS':
            ln[i].f = ln[i].d

    return ln

def nodeVisited(node, closed, optimization):
    cube1 = Cube()
    cube2 = Cube()
    cube1.faces = node.state.faces
    cube1.cubeMD5()
    for n in closed:
        cube2.faces = n.state.faces
        cube2.cubeMD5()
        if cube1.id == cube2.id:
            if optimization:
                if node.f < n.f:
                    return False
                else:
                    return True
            else:
                return True
    return False 


def createSolution(current_node):
    sol = []
    node = current_node
    while node is not None:
        sol.append(node)
        node = node.parent
    return sol

print('Introduce the json filename of the Initial_state')
filename = input()
c = Cube()
c.json2cube(filename)
Prob = Problem(c) #Clase Problem with InitialState and functions isGoal and sucessors
sol = limited_search(Prob, "DFS", 2)
print(sol)
