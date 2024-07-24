# pathfinding algorithm that generates every single route through the graph, and then selects the route that has the lowest overall cost

# works only with weighted directed acylcic graph's (DAG)

# 4 steps: 1: find the node with lowes weight (way to this node with lower cost doesn't exist!)  2:calculate (in table) costs of neighbors.   again step 1:find the lowest weight !!
# it can be way from previous node (not nesessery new one).   if the new ways to old nodes cost lower - parents of these node changes (yes, we note parents to everyone)

# negative-weight edges = no use Dijkstra alg    use Bellman-Ford algorithm

# FIRSTLY, WE NEED 3 HASH-TABLES: GRAPGH(directions+cost),  COSTS,  PARENTS

# we need to make graph in graph
graph = {}
graph["start"] = {}            # key=node, value=graph with key=nodes  values=weights
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["final"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["final"] = 5
graph["final"] = {}


infinity = float("inf")   # makes the infinity value
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["final"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["final"] = None

# ALSO WE NEED ARRAY TO KEEP PROCESSED NODES
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def main_search_shortest_way(graph, costs, parents):
    node = find_lowest_cost_node(costs)             # find cheapest node   =  b
    while node is not None:
        cost = costs[node]                         # find cost and   = 2
        neighbors = graph[node]                      #  neighbors of that node     = a,  final
        for n in neighbors.keys():                    # loop through the neighbors  i = a    = final
            new_cost = cost + neighbors[n]              #  another way to get A point
            if costs[n] > new_cost:                # is it cheaper?   6 < 5, so you find shorter path:
                costs[n] = new_cost                     # update cost
                parents[n] = node                       # update parent
        processed.append(node)
        node = find_lowest_cost_node(costs)

main_search_shortest_way(graph, costs, parents)

print("by parents u can find sequence:   ", parents)   
print("final cost is the cheapest cost by path for final:     ", costs["final"])