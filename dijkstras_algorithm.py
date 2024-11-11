""" Python implementation of Dijkstra's algorithm """


import math

# representation of a visual graph in the code
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# stores the current costs for each node
infinity = math.inf
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# stores parent of given node
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# keeps track of all nodes we already processed
processed = set()


def find_lowest_cost_node(costs):
    lowest_cost = math.inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    node_cost = costs[node]
    out_neighbors = graph[node]
    for n in out_neighbors.keys():
        new_cost = node_cost + out_neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.add(node)
    node = find_lowest_cost_node(costs)

print(f"The last node before the fin in the shortest path is: {parents['fin']}, and then shortest path "
      f"follows the order in this dict: {parents}")
