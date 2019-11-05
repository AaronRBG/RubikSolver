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