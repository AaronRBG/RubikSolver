from frontier import Frontier
from problem import Problem
from node import Node
from cube import Cube
import json
from time import time
import math
import sys

id=0

def limited_search(Prob, strategy, max_depth, visuals, optimization):
    fringe = Frontier()
    initial_node = Node(0, Prob.Initial_state, 0, "")
    initial_heuristic = generateH(initial_node)
    initial_node.f = initial_heuristic
    initial_node.h = initial_heuristic
    fringe.insertNode(initial_node)
    closed = {}
    solution = False
    cut = False
    while (solution is not True) and (fringe.isEmpty() is not True):
        current_node = fringe.removeNode()
        if visuals:
            printDepth(current_node)
        if Prob.isGoal(current_node.state):
            solution = True
        else:
            if not optimization == 2:
                cut = nodeVisited(current_node, closed, bool(optimization))
                if cut and visuals:
                    print("CUT")
                if not cut:
                    ls = Prob.successors(current_node.state)
                    ln = createListNodes(ls, current_node, max_depth, strategy) #Do createListNodes function
                    fringe.insertList(ln)
                    if optimization != 0:
                        closed[current_node.state.id]=current_node.f

            if optimization == 2:
                ls = Prob.successors(current_node.state)
                ln = createListNodes(ls, current_node, max_depth, strategy) #Do createListNodes function
                if ln is not None:
                    for node in ln:
                        if nodeVisited(node, closed, bool(optimization)):
                            if visuals:
                                print("CUT")
                        else:
                            fringe.insertNode(node)
                            closed[node.state.id]=node.f


    if solution:
        print("========== Number of created nodes: ", id-1," =============================")
        print("========== Memoria utilizada: ", sys.getsizeof(Node())*(id-1)/float(1024), " MB ===========================")
        return createSolution(current_node) #Do createSolution function
    else:
        return None

def search(Prob, strategy, max_depth, inc_depth, visuals, optimization):
    solution = None
    if strategy == 'IDS':
        current_depth = inc_depth
        while (not solution) and (current_depth <= max_depth):
            solution = limited_search(Prob, strategy, current_depth, visuals, optimization)
            current_depth += inc_depth
    else:
        solution = limited_search(Prob, strategy, max_depth, visuals, optimization)
    return solution

def generateH(node):
    N = len(node.state.faces["UP"][0])
    entropy = 0
    face_entropy = 0
    for i in node.state.faces.values():
        face_entropy = 0
        counter = [ 0 for i in range(6) ]
        for c in range(6):
            for j in i:
                for k in j:
                    if k==c:
                        counter[c]+=1
            if counter[c] > 0.0:
                color_entropy = counter[c]/(N*N) * math.log(counter[c]/(N*N),6)
                face_entropy += abs(color_entropy)
        entropy += face_entropy
    return entropy

def createListNodes(ls, current_node, max_depth, strategy):
    cost_current = current_node.cost
    d_current = current_node.d
    f_current = current_node.f
    global id
    ln = []
    for i in range(len(ls)):
        ln.append(Node())

    if d_current == max_depth:
        return None

    for i in range(len(ls)):
        #if current_node.parent is not None:
        #    print(current_node.parent.id)
        id+=1        
        ln[i].id = id
        ln[i].action = ls[i][0]
        ln[i].state = ls[i][1]
        ln[i].cost = ls[i][2] + cost_current
        ln[i].parent = current_node
        ln[i].d = d_current + 1
        if strategy == 'DFS' or strategy == 'LDS' or strategy == 'IDS':
            ln[i].f = - ln[i].d

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

def nodeVisited(node, closed, optimization):
    if node.state.id in closed.keys():
        if optimization:
            if abs(node.f) >= abs(closed[node.state.id]):
                return True
            else:
                closed[node.state.id] = node.f
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
