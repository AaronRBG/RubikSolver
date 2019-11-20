from frontier import Frontier
from problem import Problem
from node import Node
from cube import Cube
import json
from time import time
import math

id=0

def limited_search(Prob, strategy, max_depth):
    fringe = Frontier()
    global id
    initial_node = Node(0, Prob.Initial_state, 0, "", 0, 0)
    id+=1
    fringe.insertNode(initial_node)
    closed = []
    solution = False
    optimization = True
    cut = False
    visuals = True
    while (solution is not True) and (fringe.isEmpty() is not True):
        current_node = fringe.removeNode()
        if visuals:
            printDepth(current_node)
        if Prob.isGoal(current_node.state):
            solution = True
        else:
            if optimization and nodeVisited(current_node, closed, optimization, strategy):
                cut = True
                if visuals:
                    print("CUT")
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

def generateH(node):
    N = len(node.state.faces["UP"][0])
    entropy = 0
    for i in node.state.faces.values():
        counter = [ 0 for i in range(6) ]
        for c in range(6):
            for j in i:
                for k in j:
                    if k==c:
                        counter[c]+=1
            if counter[c] > 0.0:
                entropy += counter[c]/(N*N) * math.log(counter[c]/(N*N),6)

    entropy = round(-entropy,2)

    return entropy

def createListNodes(ls, current_node, max_depth, strategy):
    cost_current = current_node.cost
    d_current = current_node.d
    f_current = current_node.f

    ln = []
    for i in range(len(ls)):
        global id
        ln.append(Node())

    if d_current == max_depth:
        return None

    for i in range(len(ls)):
        global id
        ln[i].id = id
        id+=1
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
            ln[i].h = generateH(ln[i])
            ln[i].f = ln[i].h

        elif strategy == 'A*':
            ln[i].h = generateH(ln[i])
            ln[i].f = ln[i].h + ln[i].cost

        else:
            print("ERROR: Not a valid type of algorithm")
            exit

    return ln

def nodeVisited(node, closed, optimization, strategy):
    for n in closed:
        res = areEqual(node,n,optimization, strategy)
        if res:
            return True
    return False

def areEqual(node1, node2, optimization, strategy):
    if node1.state.id == node2.state.id:
        if optimization:
            if strategy == 'DFS':
                print(node1.d)
                if node1.d >= node2.d:
                    return True
            else:    
                if node1.f >= node2.f:
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
    sol.append(node)
    return sol

def printDepth(current_node):
    string = ""
    depth_string = ""
    node = current_node
    parents = []
    while node is not None:
        parents.append(node)
        node = node.parent

    for i in range(current_node.d):
        string+="_____"
        depth_string+="|_" + str(parents[current_node.d-i-1].action) + "_"
    depth_string+="|"
    print(string)
    global id
    print(depth_string + " " + str(current_node.f) + " " + str(current_node.id) + " " + str(id))