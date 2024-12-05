#!/usr/bin/env python3

import sys

# https://www.geeksforgeeks.org/python-program-for-topological-sorting/
from collections import defaultdict
 
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list) #dictionary containing adjacency List
        self.V = vertices #No. of vertices
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # neighbors generator given key
    def neighbor_gen(self,v):
        for k in self.graph[v]:
            yield k
     
    # non recursive topological sort
    def nonRecursiveTopologicalSortUtil(self, v, visited,stack):
         
        # working stack contains key and the corresponding current generator
        working_stack = [(v,self.neighbor_gen(v))]
         
        while working_stack:
            # get last element from stack
            v, gen = working_stack.pop()
            visited[v] = True
             
            # run through neighbor generator until it's empty
            for next_neighbor in gen:
                if not visited[next_neighbor]: # not seen before?
                    # remember current work
                    working_stack.append((v,gen))
                    # restart with new neighbor
                    working_stack.append((next_neighbor, self.neighbor_gen(next_neighbor)))
                    break
            else:
                # no already-visited neighbor (or no more of them)
                stack.append(v)
                 
    # The function to do Topological Sort.
    def nonRecursiveTopologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
         
        # result stack
        stack = []
 
        # Call the helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if not(visited[i]):
                self.nonRecursiveTopologicalSortUtil(i, visited,stack)
        stack.reverse()
        return stack
 
def parse_rules(lines):
    rules = []
    orders = []

    for i, line in enumerate(lines):
        if line.strip() == "":
            break
        x, y = line.split("|")
        rules.append((int(x), int(y)))

    for line in lines[i + 1:]:
        orders.append([
            int(x)
            for x in line.split(",")
        ])

    return rules, orders

def print_rules(rules, orders):
    for (x, y) in rules:
        print(f"{x} | {y}")

    for order in orders:
        print(", ".join([str(x) for x in order]))

def order_matches_rules(rules, order):
    for (x, y) in rules:
        if x not in order or y not in order:
            # print(f"{x=} or {y=} not in order")
            continue
        if order.index(x) > order.index(y):
            # print(f"{x} not before {y}")
            return 0

    return 1

def part_1(lines):
    rules, orders = parse_rules(lines)

    # print_rules(rules, orders)

    count = 0
    for order in orders:
        tmp = order_matches_rules(rules, order)
        # print(f"{order=}, result: {tmp != 0}")
        if tmp != 0:
            count += order[len(order) // 2]

    return count

def insert(n, dest, rules):
    must_be_after = []
    must_be_before = []
    pass

def fix_order(rules, order):
    rules_in_use = []
    for (x, y) in rules:
        if x not in order or y not in order:
            # print(f"{x=} or {y=} not in order")
            continue
        rules_in_use.append((x, y))

    max_no = max([max(x, y) for (x, y) in rules_in_use])
    g = Graph(max_no + 1)

    for (x, y) in rules_in_use:
        # print(f"Adding edge {x, y}")
        g.addEdge(x, y)

    result = g.nonRecursiveTopologicalSort()
    # print(order)
    result = list(filter(lambda n: n in order, result))
    # print(f"{result=}")
    return result

def part_2(lines):
    rules, orders = parse_rules(lines)

    # print_rules(rules, orders)

    count = 0
    for order in orders:
        tmp = order_matches_rules(rules, order)
        # print(f"{order=}, result: {tmp != 0}")
        if tmp != 0:
            continue
        # print(f"{order=}, result: {tmp == 0}")
        order = fix_order(rules, order)
        count += order[len(order) // 2]

    return count

def main():
    if len(sys.argv) < 2:
        print("missing required input file", file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()
        lines[-1] += "\n"

    print(f"#1: {part_1(lines)}")
    print(f"#2: {part_2(lines)}")

if __name__ == "__main__":
    main()