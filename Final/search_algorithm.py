from frontier import Frontier
from problem import Problem
from node import Node

def limited_search(Prob, strategy, max_depth):
    fringe = Frontier()
    initial_node = Node(Prob.InitialState)
    fringe.insertNode(initial_node)
    solution = False
    while (solution is not True) and (fringe.isEmpty() is not True):
        current_node = fringe.removeNode()
        if Prob.isGoal(current_node.state):
            solution = True
        else:
            ls = Prob.Successors(current_node.state)
            ln = createListNodes(ls, current_node, max_depth, strategy) #Do createListNodes function
            fringe.insertList(ln)
    
    if solution:
        return createSolution(current_node) #Do createSolution function
    else:
        return None

def search(Prob, strategy, max_depth, inc_depth):
    current_depth = inc_depth
    solution = None
    while (not solution) and (current_depth <= max_depth):
        solution = limited_search(Prob,strategy,current_depth)
        current_depth += inc_depth
    return solution

Prob = Problem(Initial_state) #Clase Problem with InitialState and functions isGoal and Successors

def createListNodes(ls, current_node, max_depth, strategy):
    cost_current = current_node.cost
    d_current = current_node.d
    f_current = current_node.f
    ln = [Node() for i in range(12)]

    if d_current == max_depth:
        return None

    for i in range(len(ls)):
        ln[i].action = ls[0]
        ln[i].state = ls[1]
        ln[i].cost = ls[2] + cost_current
        ln[i].parent = current_node
        ln[i].depth = d_current + 1
        if strategy == 'DFS':
            ln[i].f = 1 / (ln[i].d + 1)

        elif strategy == 'BFS':
            ln[i].f = ln[i].d

        elif strategy == 'UCS':
            ln[i].f = ln[i].cost

        elif strategy == 'LDS':
            ln[i].f = ln[i].d

    return ln


def createSolution(current_node):
    sol = []
    node = current_node
    while node is not None:
        sol.append(node)
        node = node.parent
    return sol
