# Implement Depth First Search


def do_DFS(graph, source):

	#Intialise a set for all visited nodes, and a stack for all unvisited nodes.

	visited, stack = set(), [source]

	#While stack is not empty
	while stack:
		#Pop the last element
		vertex = stack.pop()
		#Has this vertex been visited?
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited) # Add the next corresponding iterable of source to stack.

	return visited

graph = {'A': set(['B', 'C']),
         'B': set(['A','D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

#print do_DFS(graph, 'A')

'''
Now let's print all possible paths from source to destination
'''

def paths(graph, source, destination):

	stack = [(source, [source])] #Now our stack holds a tuple of the current vertex and the path

	while stack:

		(vertex, path) = stack.pop()

		for next in graph[vertex] - set(path): # Generator to find next unvisited node
			if next == destination: # Check if we have reached
				yield path + [next] 
			else:
				stack.append((next, path + [next])) # Else, add the next node to stack, and the value of the next node to path


print list(paths(graph, 'A', 'F'))
