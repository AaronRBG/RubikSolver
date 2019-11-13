from frontier import Frontier
from problem import Problem
from node import Node
from cube import Cube
import json
import math 
from time import time

def limited_search(Prob, strategy, max_depth):
    fringe = Frontier()
    initial_node = Node(0,Prob.Initial_state, 0, 0, 0)
    fringe.insertNode(initial_node)
    closed = []
    solution = False
    optimization = True
    cut = False
    visuals = True
    while (solution is not True) and (fringe.isEmpty() is not True):
        current_node = fringe.removeNode()
        if visuals:
            string = ""
            depth_string = ""
            for i in range(current_node.d):
                string+="____"
                depth_string+="|___"
            depth_string+="|"
            print(string)
            print(depth_string)
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
    if solution:
        return createSolution(current_node) #Do createSolution function
    else:
        return None

def search(Prob, strategy, max_depth, inc_depth):
    solution = None
    if strategy == 'IDS':
        current_depth = inc_depth
        while (not solution) and (current_depth <= max_depth):
            solution = limited_search(Prob, strategy, current_depth)
            current_depth += inc_depth
    else:
        solution = limited_search(Prob, strategy, max_depth)
    return solution

def createListNodes(ls, current_node, max_depth, strategy):
    cost_current = current_node.cost
    d_current = current_node.d
    f_current = current_node.f
    ln = [Node() for i in range(len(ls))]

    if d_current == max_depth:
        return None

    for i in range(len(ls)):
        ln[i].action = ls[i][0]
        ln[i].state = ls[i][1]
        ln[i].cost = ls[i][2] + cost_current
        ln[i].parent = current_node
        ln[i].d = d_current + 1
        if strategy == 'DFS' or strategy == 'LDS' or strategy == 'IDS':
            ln[i].f = 1 / (ln[i].d + 1)

        elif strategy == 'BFS':
            ln[i].f = ln[i].d

        elif strategy == 'UCS':
            ln[i].f = ln[i].cost

        elif strategy == 'Greedy':
            ln[i].f = generateH(ln[i])

        elif strategy == 'A*':
            ln[i].f = generateH(ln[i]) + ln[i].cost

        else:
            print("ERROR: Not a valid type of algorithm")
            exit

    return ln

def nodeVisited(node, closed, optimization):
    for n in closed:
        res = areEqual(node,n,optimization)
        if res:
            return True
    return False

def areEqual(node1, node2, optimization):
    cube1=node1.state
    cube2=node2.state
    if cube1.id == cube2.id:
        if optimization:
            if node1.f < node2.f:
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

def generateH(node):
    N = len(node.state.faces)
    for i in node.state.faces:

    entropy = 0
        for c = 0 to 5
            if counter[c] > 0.0:
                entropy += counter[c]/(N*N) * math.log(counter[c]/(N*N),6)
