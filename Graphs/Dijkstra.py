'''
Implementation of Dijkstra's algorithm, which works like so:

1) Given a directed G(v,e) with Weights(u,v) for each u to v:
	a) Initialise a dictionary of distances of each vertex from the source with infinity. Distance of source = 0.
 	b) Add all vertices to a queue.
 	c) Initialise an empty set of visited vertices. 
 	d) To get shortest path, Initialise dictionary of predecessors  

2) while queue is not empty, do:
	a) Pop from queue the vertex u with minimum distance. On the first iteration, this will be the source.
	b) Add u to Set.
	c) for each neighbour v of u:
		1) if sum(distance of u,weight(u,v)) < distance(v from source):
				update distance(v from source) with sum

3) Return (dictionary of shortest distances, dictionary of predecessors)
'''

def dijkstra(graph, source):

	dist = {}
	pred = {}
	queue = []

	#Step 1
	visited = set()

	dist[source] = 0

	for key in graph.keys():
		if key != source:
			dist[key] = float('inf')
		queue.append(key)

	#Step 2
	while queue:
		min_distance = min(queue, key = dist.__getitem__)
		min_index = queue.index(min_distance)
		
		u = queue.pop(min_index)
		
		visited.add(u)
		

		neighbours = graph[min_distance]
		

		for key in neighbours.keys():
			if((dist[u] + neighbours[key]) < dist[key]):
				dist[key] = dist[u] + neighbours[key]
				pred[key] = u
				

	return (dist, pred)


def get_shortest_path(preds, source, dest):

	path = []
	curr_vertex = dest
	while curr_vertex != source:
		path.append(curr_vertex)
		curr_vertex = preds[curr_vertex]

	path.append(source)
	path.reverse()

	return path




#Represent the graph as a dictionary of dictionaries
graph = {'Home' : {'A' : 5, 'D' : 10}, 'A' : {'B' : 2, 'C' : 7},
		  'D' : {'E' : 1, 'School' : 5}, 'E' : {'School' : 3},
		   'B' : {'School' : 3}, 'C' : {'School' : 1}, 'School' : {}}

(shortest, preds) = dijkstra(graph, 'Home')

shortest_distance = shortest['School']
shortest_path = get_shortest_path(preds, 'Home', 'School')
print "Shortest Distance : ", shortest_distance
print "Shortest Path: ",
for vertex in shortest_path:
	print vertex,

#print shortest_distance