# This program implements Breadth First Search

#Function to implement BFS

def do_BFS(graph, source):


	# Initialise list as a queue. Enqueue source.
	queue = []
	queue.append(source)

	bfs_info = []

	# Intitalise distance and predecessor of all vertices to None

	for i in range(0, len(graph)):

		bfs_info.append({'distance' : None, 'predecessor' : None})

	# Set distance of source vertex as 0	

	bfs_info[source]['distance'] = 0

	# Iterate until queue is empty
	while(len(queue) != 0):

		curr_vertex = queue.pop(0)

		# For each neighbour of current vertex
		# If neighbour has not been visited, set distance to 1 greater than current vertex
		# Set predecessor of neighbour to current vertex
		# Enqueue neighbour

		for j in range(0, len(graph[curr_vertex])):

			neighbour = graph[curr_vertex][j]

			if bfs_info[neighbour]['distance'] == None:

				bfs_info[neighbour]['distance'] = bfs_info[curr_vertex]['distance'] + 1
				bfs_info[neighbour]['predecessor'] = curr_vertex
				queue.append(neighbour)

	return bfs_info

# Create graph as an adjacency list

adjList = [[1],
    [0, 4, 5],
    [3, 4, 5],
    [2, 6],
    [1, 2],
    [1, 2, 6],
    [3, 5],
    []]

bfs_info = do_BFS(adjList, 3) # Assume source is vertex 3

for i in range(0, len(adjList)):

	print "vertex ", i, 
	print " : distance = ", bfs_info[i]['distance'],
	print " predecessor = ", bfs_info[i]['predecessor']
'''

assert bfs_info[0] == {'distance': 4, 'predecessor': 1}
assert bfs_info[1] == {'distance': 3, 'predecessor': 4}
assert bfs_info[2] == {'distance': 1, 'predecessor': 3}
assert bfs_info[3] == {'distance': 0, 'predecessor': None}
assert bfs_info[4] == {'distance': 2, 'predecessor': 2}
assert bfs_info[5] == {'distance': 2, 'predecessor': 2}
assert bfs_info[6] == {'distance': 1, 'predecessor': 3}
assert bfs_info[7] == {'distance': None, 'predecessor': None}
'''
