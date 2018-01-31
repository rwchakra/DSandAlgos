'''
This program implements Topogical Sort. It works like so:

1) Assuming we have a directed acyclic graph G(v, w), find an ordering of (v, w) s.t.
	v always preceeds w.

2) Create G(v, w) using an adjacency list, and initialise an array of visited vertices.
3) Intialise queue to store all vertices with in-degree 0.
4) while queue is not empty, 
	a) pop queue and decrement in-degrees of all its neighbours by 1.
	b) Append popped element to visited.
	c) Enqueue node with in-degree = 0.
5) Return visited
NOTE : Graph must be acyclic. One way to check this is if there are no vertices that have in-degree = 0. Return an empty list in such a case.
'''


def topsort(graph):

	# First create a dictionary of indegrees
	indegrees = {u : 0 for u in graph}
	for u in graph:
		for v in graph[u]:
			indegrees[v] += 1

	#Steps 2 and 3
	visited = []
	queue = [key for key in graph.keys() if indegrees[key] == 0]

	#Step 4
	while queue:
		curr_vertex = queue.pop()
		visited.append(curr_vertex)

		neighbours = graph[curr_vertex] # All neighbours of current vertex

		for key in neighbours: #Iterate over all neighbours of current vertex
			indegrees[key] -= 1 # Decrement indegree by 1

			if indegrees[key] == 0 and key not in queue: # If new indegree is zero, add to queue
				queue.insert(0,key)


	if len(visited) == len(graph): # Check for cycles
		return visited
	else:
		return []






'''
graph = {'A': ['B', 'D'],
         'B': ['C'],
         'C': ['D', 'E'],
         'D': ['E'],
         'E': []}

indegrees = {'A' : 0, 'B' : 1, 'C' : 1, 'D' : 2, 'E' : 2}

print topsort(graph, indegrees)
'''

build_a_house = {'foundations' : ['walls'], 'walls' : ['roof', 'windows', 'plumbing'], 
				  'roof' : ['decorating'], 'windows' : ['decorating'], 'plumbing' : ['decorating'],
				   'decorating' : []}

print topsort(build_a_house)
