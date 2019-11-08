from frontier import Frontier
from problem import Problem
from node import Node
from cube import Cube
import json
from time import time
import sys

def limited_search(Prob, strategy, max_depth, nodes, memory):
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
                if ln is not None:
                    num_nodes = 0
                    mem = 0
                    for i in range(len(ln)):
                        num_nodes += 1
                        mem += sys.getsizeof(ln[i])
                nodes += num_nodes
                memory += mem / float(1024)   #to kilobytes
                fringe.insertList(ln)
                closed.append(current_node)
            else:
                print("CUT")
    if solution:
        return createSolution(current_node), nodes, memory #Do createSolution function
    else:
        return None, nodes, memory

def search(Prob, strategy, max_depth, inc_depth):
    start_time = time()
    solution = None
    if strategy == 'IDS':
        current_depth = inc_depth
        nodes = 0
        memory = 0
        while (not solution) and (current_depth <= max_depth):
            solution, num_nodes, mem = limited_search(Prob, strategy, current_depth, nodes, memory)
            current_depth += inc_depth
            nodes += num_nodes
            memory += mem
    else:
        solution, nodes, memory = limited_search(Prob, strategy, max_depth, 0, 0)
    finish_time = time()
    print("========== Number of created nodes: ", nodes," =============================")
    print("========== Memoria utilizada: ", memory/float(1024), " MB ===========================")
    print("========== Execution time of the search: ", finish_time-start_time, " seconds ==================")
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
        if strategy == 'DFS' or strategy == 'LDS' or strategy == 'IDS':
            ln[i].f = 1 / (ln[i].d + 1)

        elif strategy == 'BFS':
            ln[i].f = ln[i].d

        elif strategy == 'UCS':
            ln[i].f = ln[i].cost

        else:
            print("ERROR: Not a valid type of algorithm")
            exit

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